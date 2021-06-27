import base64
from io import BytesIO

import numpy as np
import cv2
import imutils
from PIL import Image


class Register:
    def __init__(self, i_Image):
        self.inputImage = i_Image
        self.resizedImage = None
        self.ratio = None
        self.edged = None
        self.screenCnt = None

    def canny_Edge_Detection(self):
        self.ratio = self.inputImage.shape[0] / 500.0
        self.resizedImage = imutils.resize(self.inputImage, height=500)
        gray = cv2.cvtColor(self.resizedImage, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 70, 200)
        self.edged = edged
        return edged

    def show_Canny_Results(self):
        print("STEP 1: Edge Detection")
        cv2.imwrite(self.output_Dir + 'cannyR.jpg', self.canny_Edge_Detection())

    def find_Contours(self):
        min_area = self.edged.size

        cnts = cv2.findContours(self.edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

        max_area = 0
        for c in cnts:
            area = cv2.contourArea(c)

            if area > min_area / 10:
                peri = 0.1 * cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, peri, True)
                if area > max_area and len(approx) == 4:
                    max_area = area
                    self.screenCnt = approx

    def show_Contours(self):
        print("STEP 2: Find contours of paper")
        Contour = cv2.drawContours(self.resizedImage, [self.screenCnt], -1, (0, 255, 0), 2)
        cv2.imwrite(self.output_Dir + 'Contour.jpg', Contour)

    def transform(self):
        Warped = self.four_point_transform(self.inputImage.copy(), self.screenCnt.reshape(4, 2) * self.ratio)
        Warped = cv2.cvtColor(Warped, cv2.COLOR_BGR2GRAY)
        return Warped

    def show_TransformedImages(self):
        print("STEP 3: Apply perspective transform")
        return self.transform()

    @staticmethod
    def order_points(pts):
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        return rect

    def four_point_transform(self, image, pts):
        # obtain a consistent order of the points and unpack them
        rect = self.order_points(pts)
        (tl, tr, br, bl) = rect

        # compute the width of the new image, which will be the
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        # compute the height of the new image
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")

        # compute the perspective transform matrix and then apply it
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        # return the warped image
        return warped


def ImageRegistration(image):
    nparr = np.frombuffer(base64.b64decode(image), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    test = Register(img)
    result = test.show_TransformedImages()
    img = Image.fromarray(result, 'RGB')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    img_byte = buffered.getvalue()
    img_str = "data:image/jpeg;base64," + base64.b64encode(img_byte).decode()
    print(len(img_str))
    return img_str
