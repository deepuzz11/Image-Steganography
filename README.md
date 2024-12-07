# Image Steganography

## Overview
Image Steganography is a technique of hiding secret messages within digital images. This project demonstrates a secure method of transmitting messages by embedding them into images in a way that is imperceptible to the human eye.

## Features
- **Message Embedding:** Encode secret messages into images using Python's PIL library.
- **Message Extraction:** Decode and retrieve the hidden messages from images.
- **Text Extraction:** Use Tesseract OCR to extract text from images.
- **User-Friendly Interface:** A web application built with Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Problem Statement
Traditional encryption methods can be vulnerable to interception. This project aims to enhance the security of message transmission by using steganography to conceal messages within images.

## Hypothesis
By embedding messages in digital images using steganography, we can create a more secure communication method that is less likely to be detected by unauthorized parties.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask
- **Image Processing:** Python, PIL (Pillow)
- **Optical Character Recognition:** Tesseract OCR

## File Structure
```
Image-Steganography/
│
├── static/ # Static assets (CSS, JavaScript, images)
├── templates/ # HTML templates for the web application
├── uploads/ # Directory for storing uploaded and processed images
│
├── app.py # Main Flask application
├── encoding.py # Script for encoding messages into images
├── decoding.py # Script for decoding messages from images
├── OCR.py # Script for extracting text from images using Tesseract
├── README.md # Project documentation
├── LICENSE # License file
│
├── Encoded_Image.png # Example of an encoded image
├── Original_Image.jpg # Example of an original image
├── Original_Image_2.jpg # Another original image example
└── Blue Modern Pitch Deck Presentation.pptx # Project presentation
```
## Installation

### Install Dependencies
Ensure Python is installed on your system, then run:
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python app.py
```
Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

## Usage

### Encode a Message
1. Upload an image.
2. Enter the message to hide.
3. Save the encoded image.

### Decode a Message
1. Upload the encoded image.
2. Retrieve the hidden message.

### Extract Text from Images
1. Upload an image.
2. Use OCR to extract and view the text content.

## Results
The application was tested with various images and messages. It successfully encoded and extracted messages without any noticeable degradation in image quality, confirming steganography's potential for secure communication.

## Future Enhancements
- Improve the robustness and efficiency of the encoding/decoding process.
- Support other file formats for embedding messages.
- Add encryption for messages before embedding for added security.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Python PIL Library
- Tesseract OCR
- Flask Framework
