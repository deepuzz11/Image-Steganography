from PIL import Image

def decode_image(encoded_image_path):
    # Open the image
    encoded_image = Image.open(encoded_image_path)
    # Ensure the image is in RGB mode
    encoded_image = encoded_image.convert("RGB")

    binary_message = ""
    for y in range(encoded_image.height):
        for x in range(encoded_image.width):
            r, g, b = encoded_image.getpixel((x, y))
            binary_message += f'{r & 1}{g & 1}{b & 1}'

    # Make sure we only take full bytes and avoid padding issues
    if len(binary_message) % 8 != 0:
        binary_message = binary_message[:-(len(binary_message) % 8)]

    # Convert the binary message to a string
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == "00000000":  # Stop at a null byte
            break
        char = chr(int(byte, 2))
        if char.isprintable():  # Ensure only printable characters are included
            message += char
        else:
            break

    return message
