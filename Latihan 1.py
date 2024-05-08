import cv2
import numpy as np

img = cv2.imread('kucing.jpg')
im2 = 255 - img
cv2.imshow('kucing.jpg',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Yoga Satria Nugraha Kusmayadi
#1217070087