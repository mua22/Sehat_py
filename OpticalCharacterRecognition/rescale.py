import cv2 
import pytesseract
import numpy as np
from PIL import Image

img = cv2.imread("abe.jpg")

img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
Scl1 = clahe.apply(img)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
#_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

cv2.imshow('d',img)
cv2.waitKey(0) 
cv2.imwrite("thi.png",img)
im = Image.open("thi.png",)
im.save("this.tiff",dpi=(300.0,300.0))
img1 = cv2.imread("this.tiff")

p =pytesseract.image_to_string(img1) 

print(p)

w = open('abc.txt','w')
f = w.write(p)
w.close


