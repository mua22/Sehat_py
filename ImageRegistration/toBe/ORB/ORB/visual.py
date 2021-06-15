import cv2
import numpy as np

img1 = cv2.imread("Visualize/img.jpg") # input image
img2 = cv2.imread("Visualize/ref.jpg")  # Reference image.

image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb_detector = cv2.ORB_create(250)

kp1, d1 = orb_detector.detectAndCompute(image1, None)
kp2, d2 = orb_detector.detectAndCompute(image2, None)

kp1Img = cv2.drawKeypoints(image1, kp1, None, flags= None)
kp2Img = cv2.drawKeypoints(image2, kp2, None, flags= None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = matcher.match(d1, d2)

matches.sort(key=lambda x: x.distance)

desImg = cv2.drawMatches(image1, kp1, image2, kp2, matches[:25], None)

cv2.imshow("Matches", desImg)
cv2.imshow("KeyPoints1", kp1Img)
cv2.imshow("KeyPoints2", kp2Img)


# cv2.imwrite('Visualize/Matches/InputKeypoints.jpg', kp1Img)
# cv2.imwrite('Visualize/Matches/RefKeypoints.jpg', kp2Img)
# cv2.imwrite('Visualize/Matches/DesMatches.jpg', desImg)

cv2.waitKey(0)