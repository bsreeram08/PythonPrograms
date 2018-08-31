import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("sreeface.png",1)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
#for x,y,w,h in faces:
#    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#re=cv2.resize(img,(int(img.shape[0]/3),int(img.shape[1]/3)))
img=img[194:194+648,269:269+648]
cv2.imshow("gray",img)
cv2.imwrite("sreefinal.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
