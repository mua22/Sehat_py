from PIL import Image
import cv2
import pytesseract

black = (0,0,0)
white = (250,250,250)
threshold = (145,145,145)

# Open input image in grayscale mode and get its pixels.
img = Image.open("abd.jpg").convert("LA")

pixels = img.getdata()

newPixels = []

# Compare each pixel
for pixel in pixels:
    if pixel < threshold:
        newPixels.append(black)
    else:
        newPixels.append(white)

# Create and save new image.
newImg = Image.new("RGB",img.size)
newImg.putdata(newPixels)
newImg.save("new.jpg")



p = pytesseract.image_to_string(newImg)
print(p)
#w = open("thresh.txt",'w')
#w.write(p)
#w.close