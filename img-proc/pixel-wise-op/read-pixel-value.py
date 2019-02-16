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

# Read the pixel value from the coordinate that have just assigned
def report_coordinate_rgb_val(img, row, col):
    read_r = img[row, col, 2]
    read_g = img[row, col, 1]
    read_b = img[row, col, 0]

    # Report the value 
    print('The current coordinate' + str((row, col)))
    print('R: ' + str(read_r) + '  G: ' + str(read_g) + '  B: ' + str(read_b))

print('This is the most top-left value: ')
report_coordinate_rgb_val(img, 0, 0)    # Feel free to try to change the input coordinate! 

print('\nThis is some random coordinate: ')
report_coordinate_rgb_val(img, 200, 384)