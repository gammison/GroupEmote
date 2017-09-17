import numpy as np
import cv2
import time
import copy

cap = cv2.VideoCapture(0)

#faces = none
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


cv2.startWindowThread()
rectangleColor= (0,255,0)


while(True):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #facesprev = copy.deepcopy(faces)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    # Display the resulting frame
    cnt = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame,str(cnt),(x,y+h+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
        cnt+=1

    cv2.putText(frame,'FACES'+str(len(faces)), (0,frame.shape[0]), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('frame',frame)

    print("faces",len(faces))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break




#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
