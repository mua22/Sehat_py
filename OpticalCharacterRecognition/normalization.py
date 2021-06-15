import cv2 as cv
import numpy as ppool
import pytesseract
img = cv.imread("skmmb.jpg")
norm = ppool.zeros((8000,8000))
final = cv.normalize(img,  norm, 35, 255, cv.NORM_MINMAX)
cv.imshow('Normalized Image', final)
cv.imshow('Image', img)

cv.imwrite('norm.jpg', final)
cv.waitKey(0) 
print(pytesseract.image_to_string(final))