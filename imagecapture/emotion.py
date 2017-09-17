import cv2.face

def get (image):
    fisherFace = cv2.face.FisherFaceRecognizer_create()
    fisherFace.load('../emotion_detection_model.xml')
    return fisherFace.predict(image)
