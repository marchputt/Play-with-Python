"""
Example of how to show images in PyCharm's SciView using matplotlib.

This should work as the screen shot provided in "ss.png".
"""


import matplotlib.pyplot as plt
from skimage import io


def imshow_sk(input_skimage, cv_img_yn=0):
    """
    Easy MATLAB-like imshow function just for development and debugging based on matplotlib-pyplot

    :param input_skimage: input image compatible with skimage format
    :param bool cv_img_yn: (optional) indicate if the input image is OpenCV type (1) or not.
    :return: (Window that displays the input image)
    """
    if cv_img_yn == 1:
        # Convert OpenCV image into Scikit Image format
        input_skimage = input_skimage[:, :, ::-1]

    fig = plt.figure("Figure")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(input_skimage)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    img = io.imread('../sample-images/dog.jpg')
    imshow_sk(img)


