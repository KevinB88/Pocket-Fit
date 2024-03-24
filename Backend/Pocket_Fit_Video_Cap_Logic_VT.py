from flask import Flask, Response, render_template
import cv2
import time

app = Flask(__name__)

# face_cascade = cv2.CascadeClassifier('/Users/kbedoya88/Desktop/PROJECTS24/PyCharm/TensorFlow/TensorFlow/OpenCV/HaarCascade_XML-Files/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('/PocketFit/Pocket-Fit/HaarCascade_XML-Files/haarcascade_frontalface_alt2.xml')

# Initialize video capture from the default webcam
cap = cv2.VideoCapture(1)


def generate_frames():
    while True:
        # Capture frame-by-frame
        success, frame = cap.read()
        if not success:
            break
        else:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Reduce frame size for faster processing
            frame = cv2.resize(frame, (640, 480))  # Adjust dimensions as needed

            # Optionally, apply any quick, necessary image processing here

            # Introduce a delay to lower the frame rate
            time.sleep(0.05)  # Adjust delay to control frame rate

            # Encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            if not flag:
                continue

            # Yield each frame as a byte stream, using multipart/x-mixed-replace for MJPEG
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(encodedImage) + b'\r\n')

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


@app.route('/video_feed')
def video_feed():
    # Return the response generated along with the specific media
    # type (mime type)
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
