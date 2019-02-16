import cv2 as cv
from matplotlib import pyplot as plt


# Read the image
img = cv.imread('../sample-images/dog.jpg')

img[0, 0, 0] = 0
img[0, 0, 1] = 0
img[0, 0, 2] = 255

img[0, 1, 0] = 0
img[0, 1, 1] = 255
img[0, 1, 2] = 0

img[0, 2, 0] = 255
img[0, 2, 1] = 0
img[0, 2, 2] = 0

plt.imshow(img[:, :, ::-1])
plt.show()

# Crop the image so that we see the top-left part
img_crop = img[0:20, 0:20, :]
plt.imshow(img_crop[:, :, ::-1])
plt.show()

