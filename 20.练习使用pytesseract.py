# -*- coding: utf-8 -*-
#pytr
from pytesseract import image_to_string
from PIL import Image

img = Image.open('123.png')
img1 = Image.open('111.png')

print(image_to_string(img1))