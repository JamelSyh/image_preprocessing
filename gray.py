import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cv.namedWindow("img", cv.WINDOW_NORMAL)

# read the image
img = cv.imread("./images/gray.png", 0)
blur = cv.GaussianBlur(img, (5, 5), 0)
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(
    blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3.2)

# converting to its binary form
# reT, bn = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# resize the image

# show the initial image
# cv.imshow("img",img)


# get shape
# H, L, I = img.shape

# iterate through the images pixels and apply the gray mode filter

# for i in range(0, H):
#    for j in range(0, L):
#       B,G,R = img[i,j]

#       img[i,j] = (0.2989 * B + 0.5870 * G + 0.1140 * R)

# for i in range(0, H):
#    for j in range(0, L):
#       B, G, R = img[i, j]
#       if img[i, j] < img.any():
#         img[i, j] = [0, 0, 0]
#       else:
#         img[i, j] = img.all(255)

# show resized/filterd
cv.imshow("img", th2)
# save
# cv.imwrite('./images/P9-gray.png',img)


cv.waitKey(0)
cv.destroyAllWindows()
