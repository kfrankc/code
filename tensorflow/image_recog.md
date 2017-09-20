# Image Recognition

_Convolutional Neural Networks_ can achieve reasonable performance on hard visual recognition tasks, matching or exceeding human performance in some domains.

Some examples of successive models that show improvements:

* QuocNet
* AlexNet
* Inception
* BN-Inception-v2
* Inception-v3

## Using the Python API

```
cd models/tutorials/image/imagenet
python classify_image.py
```

To use other JPEG images, edit the `--image-file` arg

## Taking a deeper look at how this API works

Look inside `tensorflow/examples/label_image/main.cc`. The model expectes to get a 299x299 RGB image, so we have flags set to check for the width and height of the input image. In addition, the pixel values are scaled from `int` to `float`, in order for the graph to operate properly.