Please install:
* [TensorFlow >= 1.4](https://www.tensorflow.org/)
* [scikit-learn](http://scikit-learn.org/)
---
1. The following command clones all the files (>300MB);
```
git clone https://github.com/zhedongzheng/finch.git
```

2. Use [contents](https://github.com/zhedongzheng/finch#contents) to find the model and test that may interest you, click on that test
<img src="https://github.com/zhedongzheng/finch/blob/master/assets/addr_0.png" width="600">

3. Find the test file path
<img src="https://github.com/zhedongzheng/finch/blob/master/assets/addr.png" width="600">

4. run on command line
```
cd finch/nlp-models/tensorflow
python rnn_attn_estimator_imdb_test.py
```
---
#### Word Embedding
* Skip-Gram &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/word2vec_skipgram.py) &nbsp; &nbsp; [Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/word2vec_skipgram_test.py)

* CBOW &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/word2vec_cbow.py) &nbsp; &nbsp; [Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/word2vec_cbow_test.py)

#### Text Classification
* CNN &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_1d_text_clf.py) &nbsp; &nbsp; [IMDB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_1d_text_clf_imdb_test.py) &nbsp; | &nbsp; [Model (Multi-kernel)](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/concat_conv_1d_text_clf.py) &nbsp; &nbsp; [IMDB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/concat_conv_1d_text_clf_imdb_test.py) &nbsp; &nbsp; [Result](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/concat_conv_1d_text_clf_imdb_test.md)

* LSTM &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_clf.py) &nbsp; &nbsp; [IMDB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_clf_imdb_test.py)

* CNN-LSTM &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_rnn_text_clf.py) &nbsp; &nbsp; [IMDB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_rnn_text_clf_imdb_test.py)

* LSTM + Attention &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_attn_text_clf.py) &nbsp; &nbsp; [IMDB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_attn_text_clf_imdb_test.py) &nbsp; | &nbsp; [Estimator](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_attn_estimator.py) &nbsp; &nbsp; [IMDB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_attn_estimator_imdb_test.py) &nbsp; &nbsp; [IMDB Config](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_attn_estimator_imdb_config.py)

#### Sequence Labelling
* BiLSTM &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/birnn_seq2seq_clf.py) &nbsp; &nbsp; [POS Tagging Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/pos_birnn_test.py) &nbsp; &nbsp; [Chinese Segmentation Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/chseg_birnn_test.py)

    * BiLSTM + CRF &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/birnn_crf_clf.py) &nbsp; &nbsp; [POS Tagging Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/pos_birnn_crf_test.py) &nbsp; &nbsp; [Chinese Segmentation Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/chseg_birnn_crf_test.py) 

* Multihead-Attention &nbsp; &nbsp; [Modules](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/multihead_attn.py) &nbsp; &nbsp; [POS Tagging Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/multihead_attn_pos_test.py) 

   * Multihead-Attention + CRF &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/multihead_attn_clf.py) &nbsp; &nbsp; [POS Tagging Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/multihead_attn_clf_pos_test.py) &nbsp; &nbsp; [Chinese Segmentation Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/multihead_attn_clf_chseg_test.py) 

#### Text Generation
* Char-RNN &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_gen.py) &nbsp; &nbsp; [English Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_gen_test.py) &nbsp; &nbsp; [Chinese Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_gen_addr_test.py)  &nbsp; | &nbsp; [Beam-Search Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/char_rnn_beam.py) &nbsp; &nbsp; [English Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/char_rnn_beam_test.py) 

* Character-Aware CNN-RNN Language Model &nbsp; &nbsp; [Paper](https://arxiv.org/abs/1508.06615) &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/cnn_rnn_text_gen.py) &nbsp; &nbsp; [PTB Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/cnn_rnn_text_gen_test.py) 

* [Variational Recurrent Autoencoder (VRAE)](https://github.com/zhedongzheng/vae-nlp) 

#### Sequence to Sequence
* Seq2Seq &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq.py) &nbsp; &nbsp; [Sorting Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_test.py) &nbsp; | &nbsp; [Estimator](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_estimator.py) &nbsp; &nbsp; [Sorting Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_estimator_test.py) 

   * Seq2Seq + Attention &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_attn.py) &nbsp; &nbsp; [Sorting Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_attn_test.py) 

   * Seq2Seq + BiLSTM Encoder &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_birnn.py) &nbsp; &nbsp; [Sorting Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_birnn_test.py) 

   * Seq2Seq + Beam-Search &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_beam.py) &nbsp; &nbsp; [Sorting Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_beam_test.py) 

   * Seq2Seq + BiLSTM Encoder + Attention + Beam-Search &nbsp; &nbsp; [Model](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_ultimate.py) &nbsp; &nbsp; [Sorting Test](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/seq2seq_ultimate_test.py) 

* [Transformer (Attention Is All You Need)](https://github.com/zhedongzheng/finch/tree/master/nlp-models/tensorflow/attn_is_all_u_need) 
