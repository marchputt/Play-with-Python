import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((100,100,3), np.uint8)
# Show the black image 
# plt.imshow(img[:, :, ::-1])
# plt.show()

[row, col, _] = img.shape
row_half = int(row / 2)
col_half = int(col / 2)

img[0:row_half, 0:col_half, 0] = 255
img[0:row_half, 0:col_half, 1] = 0
img[0:row_half, 0:col_half, 2] = 0

# Show the result image 
plt.imshow(img[:, :, ::-1])
plt.show()

