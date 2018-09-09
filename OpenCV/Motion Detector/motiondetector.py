import cv2,time,pandas
from datetime import datetime
video=cv2.VideoCapture(0)
times=[]
status=0
prevstatus=0
df=pandas.DataFrame(columns=["Start","End"])
first_frame=None
while True:
    prevstatus=status
    status=0
    check, frame=video.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_img=cv2.GaussianBlur(gray_img,(21,21),0)
    if first_frame is None:
        first_frame=gray_img
        continue
    delta_frame=cv2.absdiff(first_frame,gray_img)
    threshold_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    (_,cnts,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            status=0
            continue
        status=1
        (x,y,h,w)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    if status==1 and prevstatus==0:
        times.append(datetime.now())
    if status==0 and prevstatus==1:
        times.append(datetime.now())
    cv2.imshow("Capturing",frame)
    cv2.imshow("Gray Frames",gray_img)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",threshold_frame)
    print(status)
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

#print(status_list)
print(len(times))
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)
video.release()
df.to_csv("Times.csv")
cv2.destroyAllWindows()
