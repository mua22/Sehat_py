import pytesseract
import cv2

img = cv2.imread('abd.jpg',0)

p=pytesseract.image_to_string(img)
print(p)
w = open('skmmd.txt','w')
f = w.write(p)
w.close
