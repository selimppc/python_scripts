import binascii
import sys


def convert():
    """HEX to image conversion"""
    if sys.argv[2]:
        data = sys.argv[2]
        data = data.strip()
        data = data.replace(' ', '')
        data = data.replace('\n', '')
        data = binascii.a2b_hex(data)
        with open('image/image.jpg', 'wb') as image_file:
            image_file.write(data)


if __name__ == '__main__':
    convert()
