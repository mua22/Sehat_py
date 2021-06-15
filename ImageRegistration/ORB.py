import cv2
import numpy as np


class ORB:
    def __init__(self, i_image, r_Image):
        self.i_image = cv2.imread(i_image)
        self.r_Image = cv2.imread(r_Image)
        self.grey_i_Image = cv2.cvtColor(self.i_image, cv2.COLOR_BGR2GRAY)
        self.grey_r_Image = cv2.cvtColor(self.r_Image, cv2.COLOR_BGR2GRAY)
        self.transformed_img = None

    def coordinates(self):
        height, width = self.grey_r_Image.shape
        return width, height

    def orb(self):
        orb_detector = cv2.ORB_create(5000)
        kp1, d1 = orb_detector.detectAndCompute(self.grey_i_Image, None)
        kp2, d2 = orb_detector.detectAndCompute(self.grey_r_Image, None)

        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(d1, d2)
        matches.sort(key=lambda x: x.distance)

        matches = matches[:int(len(matches) * 50)]
        no_of_matches = len(matches)

        p1 = np.zeros((no_of_matches, 2))
        p2 = np.zeros((no_of_matches, 2))

        for i in range(len(matches)):
            p1[i, :] = kp1[matches[i].queryIdx].pt
            p2[i, :] = kp2[matches[i].trainIdx].pt

        homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)
        self.transformed_img = cv2.warpPerspective(self.i_image,
                                                   homography, self.coordinates())

