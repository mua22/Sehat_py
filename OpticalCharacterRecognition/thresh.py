import cv2 as cv
import numpy as np
import pytesseract
img = cv.imread('abd.jpg',0)
#hsv = cv.equalizeHist(img)
#cv.imwrite('shad.png',hsv)
clahe = cv.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
cl1 = clahe.apply(img)
#_, th1 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th2 = cv.threshold(cl1, 128, 255, cv.THRESH_BINARY)

th3 = cv.adaptiveThreshold(th2, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
th4 = cv.adaptiveThreshold(th2, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
dst = cv.fastNlMeansDenoising(th3,None,11,9,21)
med = cv.medianBlur(th2,1)
src = cv.GaussianBlur(th2, (3, 3), 0)


#cv.imshow("Image", img)
#cv.imshow("Image", cl1)

cv.imshow("dst", cl1)
#cv.imshow("g", src)
#cv.imshow("med", cl1)

#cv.imshow("th2", th2)
#cv.imshow("th3", th3)
#cv.imshow("th4", th4)


#cv.imshow("dst", dst)

cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("medo.jpg", th2)




p = pytesseract.image_to_string(cl1)
print(p)
w = open("thresh12.txt",'w')
w.write(p)
w.close