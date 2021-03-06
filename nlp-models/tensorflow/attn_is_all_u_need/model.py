from config import args
from modules import *

import tensorflow as tf


def forward_pass(sources, targets, params, reuse=False):
    with tf.variable_scope('forward_pass', reuse=reuse):
        pos_enc = _get_positional_encoder()

        # ENCODER
        en_masks = tf.sign(tf.abs(sources))     

        with tf.variable_scope('encoder_embedding', reuse=reuse):
            encoded = embed_seq(
                sources, params['source_vocab_size'], args.hidden_units, zero_pad=True, scale=True)
        
        with tf.variable_scope('encoder_positional_encoding', reuse=reuse):
            encoded += pos_enc(sources, args.hidden_units, zero_pad=False, scale=False)
        
        with tf.variable_scope('encoder_dropout', reuse=reuse):
            encoded = tf.layers.dropout(encoded, args.dropout_rate, training=(not reuse))

        for i in range(args.num_blocks):
            with tf.variable_scope('encoder_attn_%d'%i, reuse=reuse):
                encoded = multihead_attn(queries=encoded, keys=encoded, q_masks=en_masks, k_masks=en_masks,
                    num_units=args.hidden_units, num_heads=args.num_heads, dropout_rate=args.dropout_rate,
                    causality=False, reuse=reuse, activation=None)
            
            with tf.variable_scope('encoder_feedforward_%d'%i, reuse=reuse):
                encoded = pointwise_feedforward(encoded, num_units=[4*args.hidden_units, args.hidden_units],
                    activation=params['activation'])

        # DECODER
        decoder_inputs = _shift_right(targets, params['start_symbol'])
        de_masks = tf.sign(tf.abs(decoder_inputs))
            
        if args.tie_embedding is True:
            with tf.variable_scope('encoder_embedding', reuse=True):
                decoded = embed_seq(decoder_inputs, params['target_vocab_size'], args.hidden_units,
                    zero_pad=True, scale=True, TIE_SIGNAL=True)
        else:
            with tf.variable_scope('decoder_embedding', reuse=reuse):
                decoded = embed_seq(
                    decoder_inputs, params['target_vocab_size'], args.hidden_units, zero_pad=True, scale=True)
        
        with tf.variable_scope('decoder_positional_encoding', reuse=reuse):
            decoded += pos_enc(decoder_inputs, args.hidden_units, zero_pad=False, scale=False)
                
        with tf.variable_scope('decoder_dropout', reuse=reuse):
            decoded = tf.layers.dropout(decoded, args.dropout_rate, training=(not reuse))

        for i in range(args.num_blocks):
            with tf.variable_scope('decoder_self_attn_%d'%i, reuse=reuse):
                decoded = multihead_attn(queries=decoded, keys=decoded, q_masks=de_masks, k_masks=de_masks,
                    num_units=args.hidden_units, num_heads=args.num_heads, dropout_rate=args.dropout_rate,
                    causality=True, reuse=reuse, activation=None)
            
            with tf.variable_scope('decoder_attn_%d'%i, reuse=reuse):
                decoded = multihead_attn(queries=decoded, keys=encoded, q_masks=de_masks, k_masks=en_masks,
                    num_units=args.hidden_units, num_heads=args.num_heads, dropout_rate=args.dropout_rate,
                    causality=False, reuse=reuse, activation=None)
            
            with tf.variable_scope('decoder_feedforward_%d'%i, reuse=reuse):
                decoded = pointwise_feedforward(decoded, num_units=[4*args.hidden_units, args.hidden_units],
                    activation=params['activation'])
        
        # OUTPUT LAYER    
        if args.tie_proj_weight is True:
            b = tf.get_variable(
                'bias', [params['target_vocab_size']], tf.float32, tf.constant_initializer(0.01))
            _scope = 'encoder_embedding' if args.tie_embedding is True else 'decoder_embedding'
            with tf.variable_scope(_scope, reuse=True):
                shared_w = tf.get_variable('lookup_table')
            decoded = tf.reshape(decoded, [-1, args.hidden_units])
            logits = tf.nn.xw_plus_b(decoded, tf.transpose(shared_w), b)
            logits = tf.reshape(logits, [tf.shape(sources)[0], -1, params['target_vocab_size']])
        else:
            with tf.variable_scope('output_layer', reuse=reuse):
                logits = tf.layers.dense(decoded, params['target_vocab_size'], reuse=reuse)
        return logits


def _model_fn_train(features, mode, params):
    logits = forward_pass(features['source'], features['target'], params)
    _ = forward_pass(features['source'], features['target'], params, reuse=True)
    log_tensors = {}

    with tf.name_scope('backward'):
        targets = features['target']
        masks = tf.to_float(tf.not_equal(targets, 0))

        if args.label_smoothing is True:
            loss_op = label_smoothing_sequence_loss(
                logits=logits, targets=targets, weights=masks, label_depth=params['target_vocab_size'])
        else:
            loss_op = tf.contrib.seq2seq.sequence_loss(
                logits=logits, targets=targets, weights=masks)

        if args.lr_decay_strategy == 'noam':
            step_num = tf.train.get_global_step() + 1   # prevents zero global step
            lr = _get_noam_lr(step_num)
        elif args.lr_decay_strategy == 'exp':
            lr = tf.train.exponential_decay(1e-3, tf.train.get_global_step(), 100000, 0.1)
        else:
            raise ValueError("lr decay strategy must be one of 'noam' and 'exp'")
        log_tensors['lr'] = lr
        log_hook = tf.train.LoggingTensorHook(log_tensors, every_n_iter=100)
        
        train_op = tf.train.AdamOptimizer(lr).minimize(loss_op, global_step=tf.train.get_global_step())
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss_op, train_op=train_op, training_hooks=[log_hook])


def _model_fn_predict(features, mode, params):
    _ = forward_pass(features['source'], features['target'], params)
    logits = forward_pass(features['source'], features['target'], params, reuse=True)
    ids = tf.argmax(logits, -1)
    return tf.estimator.EstimatorSpec(mode=mode, predictions=ids)


def tf_estimator_model_fn(features, labels, mode, params):
    if mode == tf.estimator.ModeKeys.TRAIN:
        return _model_fn_train(features, mode, params)
    if mode == tf.estimator.ModeKeys.PREDICT:
        return _model_fn_predict(features, mode, params)


def _shift_right(targets, start_symbol):
    start_symbols = tf.cast(tf.fill([tf.shape(targets)[0], 1], start_symbol), tf.int64)
    return tf.concat([start_symbols, targets[:, :-1]], axis=-1)


def _get_positional_encoder():
    if args.positional_encoding == 'sinusoidal':
        pos_enc = sinusoidal_positional_encoding
    elif args.positional_encoding == 'learned':
        pos_enc = learned_positional_encoding
    else:
        raise ValueError("positional encoding has to be either 'sinusoidal' or 'learned'")
    return pos_enc


def _get_noam_lr(step_num):
    return tf.rsqrt(tf.to_float(args.hidden_units)) * tf.minimum(
        tf.rsqrt(tf.to_float(step_num)),
        tf.to_float(step_num) * tf.convert_to_tensor(args.warmup_steps ** (-1.5)))
