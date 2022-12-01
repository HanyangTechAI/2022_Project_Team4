# importing the required libraries
from flask import Flask, request, send_file
from flask_cors import CORS
from config import config

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time

# from ..model import api

import uuid
id = uuid.uuid1()

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods = ['POST'])
def uploadfile():
    f = request.files['file']
    f.filename = str(id)
    # f.save(config.default_dir + "videos/" + str(id) + '.mp4')
    f.save("/Users/yeonukpae/Desktop/videos/" + str(id) + '.mp4')

    # resolution = request.json['resolution']
    return str(id)
  
@app.route('/time', methods = ['POST'])
def getVideoId():
    id = request.args.get('id')
    time = request.json['time']
    print(id, time)
    # api.createClass(id, time)
    return "success"

@app.route('/region', methods = ['GET'])
def returnRegion():    
    id = request.args.get('id')
    # api.getMaskedImage(id)
    # return send_file(config.default_dir + 'a.jpg', mimetype = 'image/jpg')
    return send_file('/Users/yeonukpae/Desktop/a.jpg', mimetype = 'image/jpg')

@app.route('/coordinates', methods = ['POST'])
def getCoordinates():
    id = request.args.get('id') # get the value of id (i.e. ?id=some-value)

    x = request.json['x']
    y = request.json['y']
    print(id, x, y)
    return "success"

@app.route('/mask', methods = ['GET', 'POST'])
def returnMask():    
    if request.method == 'GET':
        # selected_mask = api.getSelectedMask(id, [x, y])
        # return send_file(selected_mask, mimetype = 'image/jpg')
        # return send_file(config.default_dir + 'c.jpg', mimetype = 'image/jpg')
        return send_file('/Users/yeonukpae/Desktop/c.jpg', mimetype = 'image/jpg')
    
    # api.process(id)
    time.sleep(5)
    return "success"

@app.route('/video', methods = ['GET'])
def returnVideo():    
    id = request.args.get('id')
    # must return the processed video with id
    # return send_file(config.default_dir + 'b.mp4')
    return send_file('/Users/yeonukpae/Desktop/b.mp4')

if __name__ == '__main__':
  	app.run(host = '0.0.0.0', port = 9091) # running the flask app
