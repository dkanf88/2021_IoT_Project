import cv2

#image 파일 읽기
img = cv2.imread('selena.jpg')
img2 = cv2.resize(img,(400,600))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Edge 추출
edge1=cv2.Canny(img, 50, 100)
edge2=cv2.Canny(img, 100, 150)
edge3=cv2.Canny(img, 150, 200)
#cv2.imshow('selena', img2)
#cv2.imshow('selena_GRAY', gray)
cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

#키보드 입력을 기다림(millisecond)
#기본값 0, 0인 경우 키보드 입력이 있을 때까지 계속 기다림
#Enter : 13, ESC: 27
while True:
    #if cv2.waitKey() == ord('q'):
    if cv2.waitKey() == 13:
        break

#파일로 저장하기
cv2.imwrite('selena_GRAY.jpg', gray)

#열려있는 모든 창 닫기
cv2.dstroyAllWindows()