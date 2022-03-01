import cv2
import numpy as np
from PIL import Image

# Read First Image
img1 = Image.open('Pic1.jpg')
width, height = img1.size
img1 = img1.resize((width / 2, height / 2))

# Read Second Image
img2 = cv2.imread('Pic1.jpg')

# concatanate image Horizontally
Hori = np.concatenate((img1, img2), axis=1)

# concatanate image Vertically
Verti = np.concatenate((img1, img2), axis=0)

cv2.imshow('HORIZONTAL', Hori)
cv2.imshow('VERTICAL', Verti)

cv2.waitKey(0)
cv2.destroyAllWindows()