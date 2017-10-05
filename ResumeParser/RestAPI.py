#!/usr/bin/python3
import os

from flask_restful import Resource, Api
from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
api = Api(app)

app.config['UPLOAD_FOLDER'] = 'sample'
ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print filename
            return redirect(url_for('index'))
    return "OK"

class Welcome(Resource):
    def get(self):
        data = {'name':'Shiva Kumar', 'Company':'EPAM Systems India Pvt. Ltd.','email':'shiva2035.iiit@gmail.com','mobile':9963808956}
        return jsonify(data)

api.add_resource(Welcome, '/welcome')


if __name__ == '__main__':
    app.run(host='localhost', port=2035, debug=True)
