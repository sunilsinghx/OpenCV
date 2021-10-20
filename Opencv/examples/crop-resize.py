#To crop and resize an image 
import cv2 
#read image
img = cv2.imread(r"image-new.jpg")

print(img.shape)
#show orignal image
cv2.imshow("Orignal image",img)

#croped image
#in range first (height 100-->500) and (width 500-->1000)
cv2.imshow("Cropped image",img[100:500,500:1000])
#-----------------------------------------------------------------------------------------------
#resize image
"""
Syntax – cv2.resize()
The syntax of the cv2.resize() function is

cv2.resize(src, size,  fx, fy, interpolation)
src: (required) The path of the input image.
size: (required) The required size for the output image is given as a tuple of width and height
fx: (optional) The scaling factor for the horizontal axis.
fy: (optional) The scaling factor for the vertical axis.
interpolation: (optional) It refers to the algorithm used for scaling or resizing. The following interpolation algorithms are available:
INTER_NEAREST
INTER_LINEAR
INTER_AREA
INTER_CUBIC
INTER_LANCZOS4"""

img = cv2.imread(r"new.JPG")

print("orignal size:",img.shape)
width = 1000
height = 500


resize = cv2.resize(img,(width,height),interpolation=cv2.INTER_AREA) #INTER_AREA means shrink the image
cv2.imshow("Resized image",resize)
print("REsize size:",resize.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()