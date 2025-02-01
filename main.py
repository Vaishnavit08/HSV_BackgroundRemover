import cv2
import numpy as np

img=cv2.imread('green.jpg')
img=cv2.resize(img,(200,250))

# converting into hsv (hsv of original image)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# roi of second img
roi=cv2.imread('g.jpg')
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

# histogram of roi of secong img (g.jpg)
roi_hist=cv2.calcHist([hsv_roi],[0,1],None,[180,256],[0,180,0,256])

# masking
mask=cv2.calcBackProject([hsv],[0,1],roi_hist,[0,180,0,256],1)

# noise filtering(filtering remove noise)
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask=cv2.filter2D(mask,-1,kernel)
# threshold detection
_,mask=cv2.threshold(mask,200,255,cv2.THRESH_BINARY)

# mask merging
mask=cv2.merge((mask,mask,mask))  # for properly fixing the pixel value of an image here we are passing mask function thrice
result=cv2.bitwise_or(hsv,mask)

cv2.imshow('green',img)
cv2.imshow('mask',mask)
cv2.imshow('result',result)
cv2.imshow('HSV_Original',hsv)


cv2.waitKey(0)
cv2.destroyAllWindows()
