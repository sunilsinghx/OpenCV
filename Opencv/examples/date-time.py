#python program to display date and time in real time on webcam

import cv2
import datetime

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #capture webcam

print(f"width: {cap.get(3)}, Height: {cap.get(4)}",)

while cap.isOpened():
    ret, frame = cap.read() #capture frame and get booliean if got success/fail
    if ret == True:
        font = cv2.FONT_HERSHEY_PLAIN
        text = 'width :'+str(cap.get(3)) +'Height : '+str(cap.get(4))
        datet = str(datetime.datetime.now())    #get current date & time
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2) #img->text->position->font->scale->color->size
        #putting in frame to get updated date/time every second
        cv2.imshow("Date-Time",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #wait untill 'q' os pressedS
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

