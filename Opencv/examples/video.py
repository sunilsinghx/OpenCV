import cv2

#for webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#for video
#cap = cv2.VideoCapture(r"C:\Users\HP DR0002TX\Desktop\python Files\OpenCV\xyz.MOV")
while True:
    sucess, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
    
