"""
This is a tutorial script for adding red color to the first quarter 
area of the image.
"""
import cv2 as cv
from matplotlib import pyplot as plt    # Import for plotting purpose


img = cv.imread('../sample-images/dog.jpg')     # Read the image using OpenCV

[img_height, img_width, _] = img.shape  # Get the image shape
img_height_half = int(img_height / 2)   # Divide the height and width (n/2 value in the MATLAB book)
img_width_half = int(img_width / 2)     # (m/2 value in the MATLAB book)

# Change the value of the targetted pixels
img[0:img_height_half, 0:img_width_half, 0] = 0
img[0:img_height_half, 0:img_width_half, 1] = 0
img[0:img_height_half, 0:img_width_half, 2] = 255

# Show the image
plt.imshow(img[:, :, ::-1])
plt.show()

