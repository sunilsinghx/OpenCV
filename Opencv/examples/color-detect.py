#click on image show color of where click in image in new window

import cv2
import numpy as np 

def click_event(event,x,y,param,flag):

    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0] #taking value of blue channel
        green = img[y,x,1] #taking value of green channel
        red = img[y,x,2] #taking vlaue of red channel
        cv2.circle(img,(x,y),3,(255,0,0),-1) #img->centre->radius->color->thickness(-1 means fill the circle)
        mycoloimage = np.zeros((512,512,3),np.uint8)
        #giving color channel value to window mycolorimage where clicked in orignal image
        mycoloimage[:] = [blue,green,red]
        cv2.imshow('color',mycoloimage)


img = cv2.imread("new.JPG",cv2.CAP_DSHOW)
#img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
# points=[]

cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

