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

## Reference book 
Some of the example in this project is the Python version of examples in the book ["การประยุกต์ใช้ MATLAB สำหรับการประมวลภาพดิจิตอล"](http://www.ookbee.com/Shop/Book/9a2fd582-e920-42fc-b5a7-d600705248e1). 

The example number sorted by the book is listed here: 
* Chapter 1
  * [Example 1-1](img-proc/resize/) Resizing the image.
* Chapter 2
  * [Example 2-1](img-proc/read-write/) Reading the image.
  * Example 2-2 (See [Example 2-1](img-proc/read-write/)) Showing the image.
  * Example 2-3 Arithmetic
  * Example 2-4 Read and show multiple images. 
* Chapter 3
  * Example 3-2 Read and play a video file. 
* Chapter 4
  * [Example 4-1](img-proc/pixel-wise-op/change-pixel-value.py) Pixel-wise operation (write)
  * [Example 4-2](img-proc/pixel-wise-op/read-pixel-value.py) Pixel-wise operation (read) (See example 4-1)
  * Example 4-3 Add color to the first quarter of the image
  * Example 4-4 Generate black image, then fill the first quarter with white color. 
  * Example 4-5 Find the coordinate with specific color
  * Example 4-6 Generate one-layer and three-layer black-and-white image
  * Example 4-7 Add border (bounding box) to specific part of the image

(more chapters to come in the future!)