import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Your image")
#change color to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply the thresholding
r, thresh = cv2.threshold(gray_img, 225, 255, 0)
#Detect all contours using the below mode and detecting only the end points via mentioned method
img_contours, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#colored the contours with red lines
cv2.drawContours(img, img_contours, -1, (0,0,0))
cv2.imshow('Image Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
