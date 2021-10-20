#Dispaly Coo-rdinate on screen when click 

import cv2
import numpy as np 

#events = (for i in dir(cv2) if event in i)
#print(event)

def click_event(event,x,y,param,flag):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x," ,",y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strxy = str(x) +', '+str(y)
        cv2.putText(img,strxy,(x,y),font,0.7,(255,0,0),2) 
        cv2.imshow("image",img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]   #taking blue channel 
        green = img[x,y,1]  #taking green channel
        red = img[x,y,2]    #taking red channel
        font = cv2.FONT_HERSHEY_PLAIN
        strbgr = str(blue) +', '+str(green) + ', '+str(red)
        #image->text->coordinates->font->font-scale->color->thickness
        cv2.putText(img,strbgr,(x,y),font,1.5,(0,0,255),2)
        cv2.imshow("image",img)


#img = np.zeros((512,512,3),np.uint8)    #make black image of 512x512 dimension
img = cv2.imread("new.JPG",cv2.CAP_DSHOW)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)  #can crop manually
cv2.imshow("image",img)

cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()