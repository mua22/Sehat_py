import cv2
import numpy as np

# Open the image files.
from rootPath import get_root_path

img1_color = cv2.imread(get_root_path()+'/Public/Img_Reg_Results/img_2.jpg')  # Image to be aligned.
img2_color = cv2.imread(get_root_path()+'/Public/Img_Reg_Results/ref_2.jpg')  # Reference image.

# Convert to grayscale.
input_image = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
ref_image = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
height, width = ref_image.shape

# Initiating ORB with 5000 points/features
orb_detector = cv2.ORB_create(5000)

# Find key points and descriptors.
# The first arg is the image, second arg is the mask (which is not required in this case).
kp1, d1 = orb_detector.detectAndCompute(input_image, None)
kp2, d2 = orb_detector.detectAndCompute(ref_image, None)

# Match features between the two images.
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match the two sets of descriptors.
matches = matcher.match(d1, d2)

# Sort matches on the basis of their Hamming distance.
matches.sort(key=lambda x: x.distance)

# Take the top 50 % matches forward.
matches = matches[:int(len(matches) * 50)]
no_of_matches = len(matches)

# Define empty matrices of shape no_of_matches * 2.
p1 = np.zeros((no_of_matches, 2))
p2 = np.zeros((no_of_matches, 2))

for i in range(len(matches)):
    p1[i, :] = kp1[matches[i].queryIdx].pt
    p2[i, :] = kp2[matches[i].trainIdx].pt

# Find the homography matrix.
homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

# Use this matrix to transform the
# colored image wrt the reference image.
transformed_img = cv2.warpPerspective(img1_color,
                                      homography, (width, height))

# Save the output.
cv2.imwrite(get_root_path()+'/Public/Img_Reg_Results/ORB_output.jpg', transformed_img)