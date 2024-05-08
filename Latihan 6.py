import cv2

img = cv2.imread('otak.jpg', 1)
cv2.imshow("Original image", img)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
l_clahe = clahe.apply(l)
lab_clahe = cv2.merge((l_clahe, a, b))
img_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)
cv2.imshow('Enhanced Contrast with CLAHE', img_clahe)
cv2.waitKey(0)
cv2.destroyAllWindows()
