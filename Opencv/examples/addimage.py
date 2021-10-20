#impose image on each other

import cv2

img = cv2.imread('image-new.jpg')
img2= cv2.imread('new.JPG')

# print(img.shape)
# print(img2.size)
# print(img.dtype)

# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))

#keeping image of same size (512x512)
img= cv2.resize(img,(512,512))
img2= cv2.resize(img2,(512,512))

dst = cv2.addWeighted(img,0.8,img2,0.2,0)   #80% wight to img and 20% to img2
cv2.imshow("img",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

