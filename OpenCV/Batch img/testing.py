import cv2
img=cv2.imread("kangaroos-rain-australia_71370_990x742.jpg",0);
print(img.ndim)
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("kangaroos-rain-australia_71370_990x742",resized_image)
cv2.imwrite("kangaroos-rain-australia_71370_990x742_resized.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
