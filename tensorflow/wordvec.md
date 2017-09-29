# Vector Representations of Words

We look at the word2vec model by Mikolov et al. This model is used for learning vector representations of words, called "word embeddings"

## Motivation: Why learn word embeddings?

Image and audio processing systems work with rich, high-dimensional datasets encoded as vectors of the individual raw pixel-intensities for image data.

If we want to do tasks like object or speech recognition, we need to know the information encoded in those high-D data. It's easy for us as humans, but for NLP systems, it is difficult. This is because they treat words as **discrete atomic symbols**. However, we want to find the relationship of words with each other. 

**Key**: we need to use vector representations to understand audio, image pixels, and word context documents.

## Vector Space Models (VSMs)

VSMs represent words in a continuous vector space, where semantically similar words are mapped to nearby points (embedded next to each other). 

Predictive models will try to predict a word from its neighbors in terms of learned small, dense embedding vectors. 

Word2vec is a computationally-efficient predictive model for learning word embeddings from raw text. 