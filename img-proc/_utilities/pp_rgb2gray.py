import cv2 as cv


def convert_rgb2gray(rgb_img):
    return cv.cvtColor(rgb_img, cv.COLOR_BGR2GRAY)


if __name__ == '__main__':
    img = cv.imread('../sample-images/castle-gray_3ch.jpg')
    cv.imwrite('../sample-images/castle-gray.jpg', img)
    
    img = cv.imread('../sample-images/castle-low-contrast_3ch.jpg')
    cv.imwrite('../sample-images/castle-low-contrast.jpg', img)

