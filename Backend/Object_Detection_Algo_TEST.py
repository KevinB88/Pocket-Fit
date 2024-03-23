# Testing the capabilities of an Object-Detection Algorithm using the OpenCV library

# This program utilizes a pre-trained model: The algorithm in question: HaarCascade

import cv2

xml_file_path = '/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/TensorFlow/TensorFlow/OpenCV/HaarCascade_XML-Files/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(xml_file_path)

image = cv2.imread('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/TensorFlow/TensorFlow/OpenCV/snapshots/snapshot_20240224_231025.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()