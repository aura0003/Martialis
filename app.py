from PIL import Image
import pytesseract as pt
import numpy as np
import numpy as np
from urllib.request import Request, urlopen
import cv2

# Read image from which text needs to be extracted
req = Request(
    url = 'https://cdn.discordapp.com/attachments/1074390415618359459/1074514708213792899/image.png',
    headers={'User-Agent': 'Mozilla/5.0'}
)

wp = urlopen(req)
arr = np.asarray(bytearray(wp.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'

# Upscale and blur image
img = cv2.pyrUp(img)

# Convert to grayscale and apply Gaussian filtering
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

# Specify structure shape and kernel size.
kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
# Print extracted text
out_below = pt.image_to_string(img)
print("OUTPUT:", out_below)

# Display image
cv2.imshow('', img)
cv2.waitKey(0)
