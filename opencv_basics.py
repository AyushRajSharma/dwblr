import cv2 as cv
import numpy as np

image_path = 'image.jpg'

frame = cv.imread(image_path)
small_frame = cv.resize(frame,(1024,768))
gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
hsv_frame = cv.cvtColor(frame,cv.COLOR_RGB2HSV)
lower_red = np.array([30,50,50])
higher_red = np.array([255,50,50])
mask = cv.inRange(hsv_frame,lower_red,higher_red)
while True:
    cv.imshow('image',mask)
    if cv.waitKey(10) == ord('q'):
        break
cv.destroyAllWindows()
