import cv2 as cv

image_path = 'image.jpg'

frame = cv.imread(image_path,0)
edges = cv.Canny(frame,100,200)

while True:
    cv.imshow('edges',edges)
    if cv.waitKey(10) == ord('q'):
        break
cv.destroyAllWindows()