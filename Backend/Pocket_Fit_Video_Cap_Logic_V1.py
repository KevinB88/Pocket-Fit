# This file takes snapshots by control of the user. Pressing 'S' to take a snapshot

from flask import Flask, Response, render_template
import cv2
import time
import datetime
import os

save_directory_path = "/Users/kbedoya88/Desktop/PROJECTS24/Ivy_Hacks_2024/Project_Repo/PocketFit/Pocket-Fit/image_data_save"

if not os.path.exists(save_directory_path):
    os.makedirs(save_directory_path)

app = Flask(__name__)

# Initialize video capture from the default webcam
cap = cv2.VideoCapture(1)

current_frame = None


@app.route('/take_snapshot', methods=['POST'])
def take_snapshot():
    global current_frame
    if current_frame is not None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'snapshot_{timestamp}.png'
        save_directory = save_directory_path
        full_path = os.path.join(save_directory, filename)
        cv2.imwrite(full_path, current_frame)
        return 'Snapshot taken', 200
    return 'No frame captured', 500


def generate_frames():
    global current_frame
    while True:
        # Capture frame-by-frame
        success, frame = cap.read()
        if not success:
            break
        else:
            current_frame = frame

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

'''
    Additional steps to take:
    Allow the user to take a snapshot of an image on screen
    with the press of a button.
    
    Store the images to a directory for the moment being.
    
    The overall purpose:
    The user will take a snapshot and then the
    AI model will determine the article of clothing 
    present within the provided image.
    
    the image is loaded from the provided directory. 
    And the output is made onto the same screen. 
    

'''