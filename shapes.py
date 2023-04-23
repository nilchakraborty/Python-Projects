import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

# Drawing Function
# Draw a Circle
cv2.circle(img, (100,100), 50, (0,255,0),5)
# Draw a Rectangle
cv2.rectangle(img,(200,200),(400,500),(0,0,255),5)
#Draw a Line
cv2.line(img, (160,160),(359,29),(255,0,0),3)
#Write a Text
cv2.putText(img,"OpenCV",(160,160),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
# Displaying the Image
cv2.imshow('image', img)
cv2.waitKey(0)