import cv2
import numpy as np

img_location=r'C:\Users\Hossein\Pictures\m2.jpg'
img=cv2.imread(img_location,1)

scale_percent = 15 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)


img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted_gray=255-new_img
blured=cv2.GaussianBlur(inverted_gray,(21,21),0)
inverted_blured=255-blured
sketch=cv2.divide(new_img,inverted_blured,scale=256.0)
cv2.imshow('image',new_img)
cv2.imshow('image2',sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
