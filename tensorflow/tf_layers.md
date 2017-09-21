# A Guide to TF Layers: Building a Convolutional Neural Network

The Tensorflow `layers` model provides a high-level API that makes it easy to construct NN. We will use that API to build a NN model to recognize handwritten digits in MNIST data set.

**Note**: The MNIST dataset has 60K training examples and 10K test examples of the handwritten digits 0-9. 

## Getting Started

Create a file called `cnn_mnist.py` and add following:

```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

# Our application logic will be added here

if __name__ == "__main__":
  tf.app.run()
```

## Introduction to Convolutional Neural Networks

CNNs are the current state-of-the-art model architecture for image classification tasks. CNNs apply a series of filters to the raw pixel data of image to extract and learn higher-level features.

Here are the 3 components:

* Convolutional Layers: applies a specific number of convolution filter to the image. Convolutional layers then typically apply a ReLU activation function to the output to introduce nonlinearities into the model
* Pooling layers: downsample the image data to reduce dimensionality of feature map in order to decrease processing time. A commonly used pooling algorithm is max pooling, which extracts subregions of the feature map (e.g. 2x2-pixel tiles), keep their max value, and discards all other values
* Dense (fully connected) layers: perform classification on the features extracted by the convolutional layers and downsampled by the pooling layers.

A CNN is composed of a stack of convolutional modules that perform feature extraction. Each module consists of a convolutional layer followed by a pooling layer. 

The last convolutional module is followed by one or more dense layers that perform classification. The final dense layer in a CNN contains a single node for each target class in the model (all the possible classes the model may predict), with a softmax activation function to generate a value between 0-1 for each node. 

## Building the CNN MNIST Classifier

Let's build a model to classify the images in the MNIST dataset using the following CNN architecture.

1. Convolutional Layer #1
2. Pooling Layer #1
3. Convolutional Layer #2 
4. Pooling Layer #2
5. Dense Layer #1
6. Dense Layer #2 

The `tf.layers` module contains methods to create each of the three layer types above.

* `conv2d()` constructs a 2D convolutional layer. Takes no. of filters, filter kernel size, padding, and activation function as args
* `max_pooling2d()` constructs a 2D pooling layer using max-pooling algorithm. Takes pooling filter size and stride as args
* `dense()` constructs a dense layer. Takes no. of neurons and activation function as args