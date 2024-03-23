import cv2
import subprocess
import random
import threading
import time


def speak(voice, message):
    subprocess.run(['say', '-v', voice, message])


# Debouncing method
last_reply_time = 0

# Min interval between replies in seconds: in this example it is 5 seconds
min_interval = 5


def spotting_reply(voice):
    global last_reply_time
    current_time = time.time()
    if current_time - last_reply_time < min_interval:
        return
    last_reply_time = current_time
    replies = ['You are going to fail every single class that you take', 'Go to hell you stupid son of a bitch', 'You are  ugly', 'You suck', 'I bet you smell... Like really bad', 'You look like the shit I would fine floating in a bathroom toilet in Kiely Hall...', 'Do you think you are cool or something?']

    # replies_gian = ['Hello GianCarlo', 'You look very sexy today', 'Hey guys look at this guy, what a handsome chap.. I bet he knows how to code', 'I love you GianCarlo, I honestly really do', 'You look like my crush, oh wait you actually are..', 'Oh my god, guys, wow, GianCarlo Forero is here!']
    # reply = replies[random.randint(0, len(replies)-1)]
    reply = replies[random.randint(0, len(replies)-1)]
    speak(voice, reply)
    time.sleep(1)


# Another method to optimize performance, and to mitigate excessive back-logging

''' 
    Optimization #1 

    Keeping track of the active threads and limiting the number of concurrent replies
    Checking active thread counts / using a 'semaphore'

    max_threads = 1
    semaphore = threading.Semaphore(max_threads)
    
    def spotting_reply(voice):
        with semaphore:
        replies = ['I can see you!', 'Peekaboo!', 'Oh hello there!', 'Hi! How are you?']
        reply = replies[random.randint(0, len(replies)-1)]
        speak(voice, reply)

'''


'''
    Optimization #2
    
    from concurrent.futures import ThreadPoolExecutor
    
    executor = ThreadPoolExecutor(max_workers=1)
    
    def spotting_reply(voice):
    
    
    within the for-loop:
    
    for(x, y, w, h) in faces:
        executor.submit(spotting_reply, 'Daniel')


'''


face_cascade = cv2.CascadeClassifier('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/TensorFlow/TensorFlow/OpenCV/HaarCascade_XML-Files/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        threading.Thread(target=spotting_reply, args=('Whisper', )).start()

    cv2.imshow('Face Detection in Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

