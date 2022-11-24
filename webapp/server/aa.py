import os
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
CORS(app)

# 파일 업로드
@app.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save('./uploads/'+ filename)
    print(file)
    return "success"

@app.route('/time_flame', methods=['POST'])
def time_upload():
    data = request.get_json()
    print(data)
    print(data['time'])
    return "success"

@app.route('/getXY', methods=['POST'])
def xy_upload():
    data = request.get_json()
    print(data)
    print(data['coordinateX'])
    print(data['coordinateY'])
    return "success"

@app.route('/fileDownload/<filename>', methods=['GET'])
def Download_File(filename: str):
    FILE_PATH = os.path.join(BASE_DIR, filename)
    return send_file(FILE_PATH, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')