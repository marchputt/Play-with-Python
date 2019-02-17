# Play with Python and a bit of image processing
This repository will contain the code produced during experimenting with python and image processing. 

## Get started 

Install Jupyter notebook
Please follow [the official guideline](https://jupyter.readthedocs.io/en/latest/install.html)

Install necessary libraries using _**pip**_. 
```bash
pip install -r requirements.txt
```

## Getting around this project
### Pure python 
The script contain example in using python is in the folder `python-demo/`. 

### Image processing
Go to `img-proc/` and explore

#### Index
* [Basic read and write](img-proc/read-write/)
* [Generating (interesting) images](img-proc/sample-images/generate-images.py)
* Geometric transformation
  * [Resizing](img-proc/resize)
* Histogram
  * [Visualizaing image histogram](img-proc/image-histogram/)
* [Pixel-wise operations](img-proc/pixel-wise-op/pixel-wise-can-do-anything.ipynb)
  * [How to access pixel value](img-proc/pixel-wise-op/read-pixel-value.py)
  * [Adding color](img-proc/pixel-wise-op/add-color.py)
  * [Modify pixel value](img-proc/pixel-wise-op/change-pixel-value.py)

## Reference book 
Some of the example in this project is the Python version of examples in the MATLAB book ["การประยุกต์ใช้ MATLAB สำหรับการประมวลภาพดิจิตอล"](http://www.ookbee.com/Shop/Book/9a2fd582-e920-42fc-b5a7-d600705248e1). 

The example number sorted by the book is listed here: 
* Chapter 1
  * [Example 1-1](img-proc/resize/opencv-imresize.ipynb) Resizing the image.
* Chapter 2
  * [Example 2-1](img-proc/read-write/) Reading the image.
  * Example 2-2 (See [Example 2-1](img-proc/read-write/read-write.ipynb)) Showing the image. (NB)
  * Example 2-3 Arithmetic
  * Example 2-4 Read and show multiple images. 
* Chapter 3
  * Example 3-2 Read and play a video file. 
* Chapter 4
  * [Example 4-1](img-proc/pixel-wise-op/change-pixel-value.py) Pixel-wise operation (write)
  * [Example 4-2](img-proc/pixel-wise-op/read-pixel-value.py) Pixel-wise operation (read) (See example 4-1)
  * [Example 4-3](img-proc/pixel-wise-op/add-color.py) Add color to the first quarter of the image
  * [Example 4-4](img-proc/the-matlab-book/ex4-4.py) Generate black image, then fill the first quarter with white color. 
  * Example 4-5 Find the coordinate with specific color
  * Example 4-6 Generate one-layer and three-layer black-and-white image [See "Pixel-wise can do anything"](img-proc/pixel-wise-op/pixel-wise-can-do-anythin.ipynb) (NB)
  * Example 4-7 Add border (bounding box) to specific part of the image
* Chapter 6
  * [Example 6-1](img-proc/image-histogram/using-image-histogram.ipynb) (NB)
  * [Example 6-2&3](Adjust [Example 6-1](img-proc/image-histogram/using-image-histogram.ipynb)) (NB)
  * [Example 6-4](img-proc/_utilities/pp_rgb2gray.py) Convert RGB image to grayscale image. 
  * Example 6-5 Create vertical and horizontal histogram from B&W image. 
* Chapter 7
  * [OpenCV tutorial](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html#dilation): They have a very good documentation. 
  * [Erosion and dilation](img-proc/morphological-op/erosion-dilation.ipynb) (NB)

NB = Jupyter Notebook
(more chapters to come in the future!)