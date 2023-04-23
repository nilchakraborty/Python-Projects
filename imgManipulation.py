import cv2
import numpy as np

image = cv2.imread("images/lion.jpg")
# fastNlMeansDenoisingColored() removes noise and smooths the image
# Parameters: image, None, h, hForColorComponents, templateWindowSize, searchWindowSize
dst = cv2.fastNlMeansDenoisingColored(image, None, 50, 20, 7, 15)

display = np.hstack((image, dst))
cv2.imshow('Original vs De-noised', display)
cv2.waitKey(0)