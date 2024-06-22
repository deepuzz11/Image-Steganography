from PIL import Image

def decode_image(encoded_image_path, original_image_path):
    original_image = Image.open(original_image_path)
    width, height = original_image.size
    encoded_image = Image.open(encoded_image_path)
    decoded_message = ''

    pixel_data = encoded_image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixel_data[x, y]
            decoded_char = chr(r & 1 | (g & 1) << 1 | (b & 1) << 2)
            decoded_message += decoded_char

    # Strip any trailing null characters from the decoded message
    message = decoded_message.rstrip('\x00')
    return message

# def main():
#     encoded_image_path = 'static/images/Encoded_Image.png'
#     original_image_path = 'Original_Image.jpg'

#     decoded_message = decode_image(encoded_image_path, original_image_path)
#     print("Decoded message:", decoded_message)

# if __name__ == '__main__':
#     main()
