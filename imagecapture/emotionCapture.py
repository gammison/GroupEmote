import numpy as np
import cv2
import time
import dlib

cap = cv2.VideoCapture(0)

#faces = none
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
#The deisred output width and height
OUTPUT_SIZE_WIDTH = 640
OUTPUT_SIZE_HEIGHT = 480


cv2.startWindowThread()
rectangleColor= (0,255,0)

#corrolation tracker
tracker = dlib.corrolation_tracker()

while(True):
        #Retrieve the latest image from the webcam
    rc,fullSizeBaseImage = cap.read()

    #Resize the image to 320x240
    baseImage = cv2.resize( fullSizeBaseImage, ( 320, 240))

    #Check if a key was pressed and if it was Q, then destroy all
    #opencv windows and exit the application
    pressedKey = cv2.waitKey(2)
    if pressedKey == ord('q'):
        cv2.destroyAllWindows()
        exit(0)


    # Capture frame-by-frame
    resultImage = baseImage.copy()
    gray=cv2.cvtColor(baseImage,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.3,5)

    #get and track the largest face
    maxArea = 0
    x=0
    y=0
    h=0
    w=0

    for (cx,cy,ch,cw) in faces:
        if cw*ch > maxArea:
            x=cx
            y=cy
            h=ch
            w=cw
            maxArea=w*h

    if maxArea > 0:
        cv2.rectangle(resultImage, (x-10, y-20), (x+w+10, y+h+20),rectangleColor,2)

    #resize the base image up
    large = cv2.resize(resultImage,(OUTPUT_SIZE_WIDTH,OUTPUT_SIZE_HEIGHT))
    cv2.imshow("resultImage",large)





"""    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesprev = copy.deepcopy(faces)
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

    print("%d faces",len(faces))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break """




# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
