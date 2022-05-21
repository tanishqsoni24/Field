import cv2
img=cv2.imread("IMG_20210715_184718.jpg")
window_name='Image'
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ims=cv2.resize(img1,(960,540))
cv2.imshow(window_name,ims)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)