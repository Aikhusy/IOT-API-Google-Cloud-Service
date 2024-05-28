from flask import Flask, request, jsonify, send_file
import numpy as np
from preprocessing import preprocessing
import pytesseract 
import cv2
import io
import numpy
from PIL import Image
# from google.colab import auth

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return("yes")

# @app.route('/login',methods=['POST'])
# def login():
#     auth.authenticate_user()
    


@app.route('/read', methods=['GET'])
def read():
    # if 'file' not in request.files:
    #     return jsonify({"error": "No file part"})

    # file = request.files['file']

    # if file.filename == '':
    #     return jsonify({"error": "No selected file"})

    image = cv2.imdecode(np.fromfile('meteranExamplex.jpg', np.uint8), cv2.IMREAD_UNCHANGED)

    ready=preprocessing(image)

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    text = pytesseract.image_to_string(ready)

    # _, img_encoded = cv2.imencode('.jpg', ready)
    # img_bytes = img_encoded.tobytes()
    # img_io = io.BytesIO(img_bytes)

    return text





if __name__ == '__main__':
    app.run('0.0.0.0' ,debug=True)