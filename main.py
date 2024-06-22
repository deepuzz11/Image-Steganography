from encoding import encode_message
from decoding import decode_image
from OCR import extract_text_from_image

def main():
    image_path = 'Original_Image.jpg'
    message_to_hide = "Hello, steganography!"

    # Encode message into the image
    encode_message(image_path, message_to_hide)

    # Decode message from the encoded image
    encoded_image_path = 'Encoded_Image.png'
    decoded_message = decode_image(encoded_image_path, image_path)
    print("Decoded message:", decoded_message)

    # Extract text from the encoded image using OCR
    extracted_text = extract_text_from_image(encoded_image_path)
    print("Extracted text from image:", extracted_text)

if __name__ == '__main__':
    main()
