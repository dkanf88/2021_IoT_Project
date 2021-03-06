import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('./xml/face.xml')


if not cap.isOpened():
    print('Camera open failed')
    exit()


#ret, frame = cap.read()
#cv2.imshow('frame', frame)
#cv2.imwrite('output.jpg', frame)
#cv2.waitkey(0)

while True:
    ret, img = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (255 ,0, 0), 2)
    

    cv2.imshow('video', img)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()