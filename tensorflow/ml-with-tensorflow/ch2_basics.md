# Chapter 2 - ML with Tensorflow

## Ch 2.1: Defining tensors

```
import tensorflow as tf
import numpy as np
```

We can define a 2x2 matrix in different ways.

```
m1 = [[1.0, 2.0],
	  [3.0, 4.0]]
m2 = np.array([[1.0, 2.0],
			   [3.0, 4.0]], dtype=np.float32)
m3 = tf.constant([[1.0, 2.0],
	  			  [3.0, 4.0]])
```

The first will be a list type, the second a numpy.ndarray type, and the third is the tensorflow.python.frameowrk.ops.Tensor type. Pretty long...

We can use a function called `convert_to_tensor(...)` like this:

```
t1 = tf.convert_to_tensor(m1, dtype=tf.float32)
t2 = tf.convert_to_tensor(m2, dtype=tf.float32)
t3 = tf.convert_to_tensor(m3, dtype=tf.float32)
```

Now, all of them are converted to the third type!