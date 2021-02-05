import binascii
import sys


def convert():
    """image to HEX conversion"""
    if sys.argv[2]:
        filename = sys.argv[2]  # 'image/chapter-2.png'
        with open(filename, 'rb') as f:
            content = f.read()
        print(binascii.hexlify(content))


if __name__ == '__main__':
    convert()
