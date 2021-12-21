import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()
#fourcc(four character code)
#DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D', 'I', 'V', 'X')
#ret, frame = cap.read()
#cv2.imshow('frame', frame)
#cv2.imwrite('output.jpg', frame)
#cv2.waitkey(0)

out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(10) == 13:
        break

cap.release()
out.release() 
cv2.destroyAllWindows()
