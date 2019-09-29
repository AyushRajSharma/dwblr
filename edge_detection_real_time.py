import cv2 as cv 

cap = cv.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,100,200)
    cv.imshow('edges',edges)
    if cv.waitKey(10) == ord('q'):
        break
cv.destroyAllWindows()
