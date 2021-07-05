import os
from flask import Flask, request, redirect, url_for, flash,jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    return 'Welcome'

@app.route('/getfile', methods=['POST'])

def getfile():
    file = request.files['file']
    return file.read()
  

if __name__ == '__main__':
    app.run(host = '0.0.0.0')




