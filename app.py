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
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit for uploaded files

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
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
        return redirect(url_for('upload_image', filename=filename))
    
    return render_template('encode.html', filename=filename)

@app.route('/decode/<filename>')
def decode_route(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(image_path):
        return "File not found. Please upload an image first."
    
    decoded_message = decode_image(image_path)
    return render_template('decode.html', filename=filename, decoded_message=decoded_message)

@app.route('/extract/<filename>')
def extract_route(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(image_path):
        return "File not found. Please upload an image first."
    
    extracted_text = extract_text_from_image(image_path)
    return render_template('extract.html', filename=filename, extracted_text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
