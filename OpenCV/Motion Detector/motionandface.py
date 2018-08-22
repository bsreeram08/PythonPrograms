import cv2
def Enquiry(lis1):
    if len(lis1) == 0:
        return 1
    else:
        return 0
video=cv2.VideoCapture(0)
first_frame=None
first_face=None
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    check, frame=video.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray1_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_img=cv2.GaussianBlur(gray_img,(21,21),0)
    if first_frame is None:
        first_frame=gray_img
        continue
    delta_frame=cv2.absdiff(first_frame,gray_img)
    threshold_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    (_,cnts,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        if first_face is None:
            first_face=face_cascade.detectMultiScale(gray1_img,scaleFactor=1.2,minNeighbors=5,minSize=(30, 30))
            if Enquiry(first_face):
                first_face=None
            else:
                cv2.imwrite("firstface.jpg",first_face)
        (x,y,h,w)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Capturing",frame)
    #cv2.imshow("Gray Frames",gray_img)
    #cv2.imshow("Delta Frame",delta_frame)
    #cv2.imshow("Threshold Frame",threshold_frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
