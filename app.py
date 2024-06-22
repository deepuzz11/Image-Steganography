import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from encoding import encode_message
from decoding import decode_image
from OCR import extract_text_from_image

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_image', filename=filename))
    
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def upload_image(filename):
    return render_template('upload.html', filename=filename)

@app.route('/encode/<filename>', methods=['GET', 'POST'])
def encode(filename):
    if request.method == 'POST':
        message = request.form['message']
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        encode_message(image_path, message)
        return redirect(url_for('index'))
    
    return render_template('encode.html')

@app.route('/decode/<filename>')
def decode(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    encoded_image_path = 'static/images/Encoded_Image.png'
    decoded_message = decode_image(encoded_image_path, image_path)
    return decoded_message

@app.route('/extract/<filename>')
def extract(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    extracted_text = extract_text_from_image(image_path)
    return extracted_text

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)
