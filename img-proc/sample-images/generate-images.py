import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt


row = 100
col = 200
img_black = np.zeros((row, col), np.uint8)
img_white = img_black.copy()
img_white[:, :] = 255
img_gray = img_black.copy()
img_gray[:, :] = 125
img_square = img_black.copy()
img_square[25:75, 125:175] = 255

img_grad = img_black.copy()     # grad = gradient
for col_ in range(col):
    col_val = int((col_/col) * 255)
    for row_ in range(row):
        img_grad[row_, col_] = col_val

# Write the image 
cv.imwrite('black.jpg', img_black)
cv.imwrite('white.jpg', img_white)
cv.imwrite('gray.jpg', img_gray)
cv.imwrite('gradient.jpg', img_grad)
cv.imwrite('square.jpg', img_square)

