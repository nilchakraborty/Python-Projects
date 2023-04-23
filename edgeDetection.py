import cv2
import numpy as np

image = cv2.imread("color.jpg") # imread() reads the image from the specified file

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # convert to grayscale
canny_image = cv2.Canny(gray,150, 200) # detect edges

kernel = np.ones((5,5), np.uint8) # create a kernel of 5x5, unit8 is the data type
dilate_image = cv2.dilate(canny_image, kernel, iterations=1) # dilate the image to increase the thickness of the edges

kernel = np.ones((1,1), np.uint8)
erode_image = cv2.erode(dilate_image, kernel, iterations=1) # erode the image to decrease the thickness of the edges

display = np.hstack((canny_image,dilate_image,erode_image)) # stack the images horizontally
cv2.imshow('Edges - Dilation - Erosion', display)
cv2.waitKey(0)