from sys import stdout
import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from utils import base64_to_pil_image
from cv2 import cvtColor,COLOR_RGB2BGR,putText,imencode,FONT_HERSHEY_TRIPLEX
from base64 import b64encode
from numpy import array,zeros
from model import Model
from time import time

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout))
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)
predictor = Model()


@socketio.on('input image', namespace='/test')
def test_message(input):
    # start = time()
    input = input.split(",")[1]
    image_data = input # Do your magical Image processing here!!
    img = base64_to_pil_image(image_data)
    img = array(img)
    test_img = cvtColor(img, COLOR_RGB2BGR)
    prediction = predictor.predict(test_img)

    # end = time()
    # print(end-start)
    emit('out-image-event', {'image_data': prediction}, namespace='/test')


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app,port=8080)
    # socketio.run(app,host = '0.0.0.0' ,port=8080)
