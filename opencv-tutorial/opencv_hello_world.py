'''

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import cv2

img = cv2.imread('dog_sample.jpg')
print(img.shape)
cv2.imshow("Title",img)
cv2.waitKey()

'''
'''
import cv2

dog_img = cv2.imread('dog_sample.jpg')
print(dog_img.shape)

while True:

    cv2.imshow('Pupppy',dog_img)
    cv2.rectangle(dog_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
'''

