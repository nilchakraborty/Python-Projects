# pip install opencv-python  
import cv2

#colorful image - 3 channels
image = cv2.imread("images/color.jpg") # imread() reads the image from the specified file
cv2.imshow('original', image) # imshow() displays an image in the specified window
print(image.shape) # shape returns a tuple of number of rows, columns and channels

#grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
print(gray.shape)

#HSV Image
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print(HSV.shape)
cv2.imshow('HSV', HSV)
cv2.waitKey(0) # waitKey() waits for a key event infinitely (when argument is 0)


'''
output will be like this:
(300, 300, 3) # 300 rows, 300 columns and 3 channels (BGR)
(300, 300) # 300 rows and 300 columns
(300, 300, 3) # 300 rows, 300 columns and 3 channels (HSV)
'''