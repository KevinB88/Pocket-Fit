# This file takes snapshots by control of the user. Pressing 'S' to take a snapshot

from flask import Flask, Response, render_template, jsonify, send_from_directory
from flask_cors import CORS
import sys
import cv2
import time
import datetime
import os

save_directory_path = "/Users/farnazinnia/Pocket-Fit/image_data_save"

app = Flask(__name__)
CORS(app)
CORS(app)

# Initialize video capture from the default webcam
camera_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0
cap = cv2.VideoCapture(camera_index)
camera_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0
cap = cv2.VideoCapture(camera_index)

current_frame = None


@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('/Users/kbedoya88/Desktop/PROJECTS24/Ivy_Hacks_2024/Pocket-Fit/image_data_save', filename)


@app.route('/get-images', methods=['GET'])
def get_images():
    image_directory = '/Users/kbedoya88/Desktop/PROJECTS24/Ivy_Hacks_2024/Pocket-Fit/image_data_save'
    images = [img for img in os.listdir(image_directory) if img.endswith((".png", ".jpg", "jpeg"))]
    return jsonify(images)


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
