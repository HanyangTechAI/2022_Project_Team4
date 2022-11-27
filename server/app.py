# importing the required libraries
from flask import Flask, request, send_file
from flask_cors import CORS
from config import config

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ..model import api

import uuid
id = uuid.uuid1()

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods = ['POST'])
def uploadfile():
    f = request.files['file']
    f.filename = str(id)
    f.save(config.default_dir + "videos/" + str(id) + '.mp4')
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
    return send_file(config.default_dir + 'a.jpg', mimetype = 'image/jpg')

@app.route('/coordinates', methods = ['POST'])
def getCoordinates():
    # here we want to get the value of id (i.e. ?id=some-value)
    id = request.args.get('id')
    x = request.json['x']
    y = request.json['y']
    print(id, x, y)
    return "success"

@app.route('/mask', methods = ['GET', 'POST'])
def returnMask():
    # selected_mask = api.getSelectedMask(id, [x, y])
    # return send_file(selected_mask)
    
    if request.method == 'GET':
        return send_file(config.default_dir + 'c.jpg', mimetype = 'image/jpg')
    
    # if request.json['isConfirmed']:
    # api.process(id)
    return "success"

@app.route('/video', methods = ['GET'])
def returnVideo():    
    id = request.args.get('id')
    # return processed video with id
    return send_file(config.default_dir + 'b.mp4')

if __name__ == '__main__':
  	app.run(host = '0.0.0.0', port = 9091) # running the flask app
