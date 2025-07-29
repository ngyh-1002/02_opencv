import cv2
import numpy as np
import matplotlib.pylab as plt

# img = cv2.imread('../img/kari-shea-FilM6ng7VGQ-unsplash.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('../img/like_lenna.png')
cv2.imshow('img', img)

channels = cv2.split(img)
colors = ('b', 'g', 'r')
for (ch, color) in zip (channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0,256])
    plt.plot(hist)

#hist = cv2.calcHist([img], [0], None, [256], [0,256])
#plt.plot(hist)

#print("hist.shape", hist.shape)
#print("hist.sum", hist.sum(), "img.shape : ", img.shape)

plt.show()