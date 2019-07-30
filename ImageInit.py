import cv2
import os, random
import numpy as np
import matplotlib.pyplot as mplt

#file = "diaretdb1_image0" + str((random.randrange(1, 89))) + ".png"
file = "diaretdb1_image081.png"

image = cv2.imread(os.path.join("D:\College\DiabeticRetinopathyML\ddb1_v02_01\images", file),0)
image_width, image_height = image.shape[:2]
dim = (512,512)#(int(image_width/2), int(image_height/2))

image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

normalizedImg = np.zeros((512, 512))
normalizedImg = cv2.normalize(image,  normalizedImg, 0, 255, cv2.NORM_MINMAX)

'''
CODE FOR EQUILIZATION OF IMAGE
equ = cv2.equalizeHist(image)
res = np.hstack((image,equ)) #stacking images side-by-side
cv2.imshow('res.png',res)
'''
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE()#(clipLimit=40.0, tileGridSize=(16, 16))# Make changes in parameters here to change contrast

cl1 = clahe.apply(image)
#cv2.GaussianBlur(cl1,(5,5),0)
res = np.hstack((image, cl1)) #stacking images side-by-side
cv2.imshow(file+' Fundus Image And CLAHE', res)
cv2.waitKey(0)
