# coding:utf-8

import pytesseract
from PIL import Image

image = Image.open('code.png')
# 设置teseract的安装路径
pytesseract.tesseract_cmd = 'E:\\Program Files (x86)\\Tesseract-OCR'
code = pytesseract.image_to_string(image)
print(code)
