import cv2, time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
sreeface=cv2.imread("sreefinal.png",0)
print(sreeface)
while True:
    check, frame=video.read()
    #print(check)
    #print(frame)
    #time.sleep(3)
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_img=face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)
    #print(type(faces))
    #print(faces)
    for x,y,w,h in gray_img:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Capturing",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
