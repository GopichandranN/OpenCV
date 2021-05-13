import cv2
import numpy as np
img=cv2.imread('assets/Default.jpg',1)
img=cv2.resize(img,(400,400)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()