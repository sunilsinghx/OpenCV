#save video from webcam 

import cv2

cap = cv2.VideoCapture(0)   #choosing webcam for video capture
fourcc = cv2.VideoWriter_fourcc(*'XVID')    #idk video codec maybe
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))   #output into file output.mp4 (20-->frame/sec),(640,480 is dimenstion)

print(cap.isOpened())

while (cap.isOpened()):
        ret , frame = cap.read()        #take (ret == booloean value T/F if frame is capture) 
        if ret == True:
            out.write(frame)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
            cv2.imshow("frame",gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break   
        else:
            break

cap.release()
out.release()
cv2.destroyAllWindows() 