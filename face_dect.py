import cv2 as cv 


cascade_path = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = cascade_path.detectMultiScale(gray,1.1,2)
    for (x,y,w,h) in  faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
    cv.imshow('video',frame)
    k = cv.waitKey(30)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
