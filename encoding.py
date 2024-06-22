from PIL import Image

def encode_message(image_path, message):
    # Open the original image
    image = Image.open(image_path)
    width, height = image.size
    
    # Convert message to binary string
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Check if message length exceeds maximum capacity
    if len(binary_message) > width * height * 3:
        raise ValueError("Message too long to encode in the image")
    
    data_index = 0
    encoded_pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = encoded_pixels[x, y]

            # Encode message into the least significant bit of each color component
            if data_index < len(binary_message):
                r = r & ~1 | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                g = g & ~1 | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                b = b & ~1 | int(binary_message[data_index])
                data_index += 1

            encoded_pixels[x, y] = (r, g, b)

            # Break out of loops if message is fully encoded
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break
    
    # Save the encoded image
    image.save('Encoded_Image.png')

# # Example usage
# def main():
#     image_path = 'Original_Image.jpg'
#     message_to_hide = "Hello, steganography!"

#     encode_message(image_path, message_to_hide)

# if __name__ == '__main__':
#     main()
