"""Program to detect face from webcam and to show name(user) on top of rectange
By pressing 's' it will save identified image in Face directory"""


import cv2

#############################################
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
color = (255,0,255)
font = cv2.FONT_HERSHEY_DUPLEX
###############################################



name = input("Enter your name: ")

cap = cv2.VideoCapture(0)
cap.set(10,150)

while cap.isOpened():
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=8)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),3)
        cv2.putText(frame,name,(x,y-5),font,1,color,2)
        imgRoi = frame[y:y+h, x:x+h]


    cv2.imshow("Result", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"Face/{name}"+".jpg",imgRoi)
        cv2.rectangle(frame,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(frame,"Image Saved",(150,265),font,2,(0,0,255),2)
        cv2.imshow("Result",frame)
        cv2.waitKey(800)
        break

    # cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
        
    
cap.release()
cv2.destroyAllWindows()
