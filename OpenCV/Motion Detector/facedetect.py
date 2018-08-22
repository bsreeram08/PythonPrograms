import cv2
import os
import sys
from string import Template

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)
for infname in sys.argv[2:]:
   image_path = os.path.expanduser(infname)
   image = cv2.imread(image_path)
   faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor, minNeighbors = min_neighbors,minSize = min_size)
   for( x, y, w, h ) in faces:
     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
     outfname = "/tmp/%s.faces.jpg" % os.path.basename(infname)
     cv2.imwrite(os.path.expanduser(outfname), image)
