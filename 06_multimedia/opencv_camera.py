import cv2

cap = cv2.VideoCapture('output.avi')



if not cap.isOpened():
    print('Camera open failed')
    exit()


#ret, frame = cap.read()
#cv2.imshow('frame', frame)
#cv2.imwrite('output.jpg', frame)
#cv2.waitkey(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()
