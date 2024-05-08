import cv2 
import numpy as np

img = cv2.imread('otak.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('MRI Image - Original vs. Equalized', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Yoga Satria Nugraha Kusmayadi
#1217070087