import pytesseract
from PIL import Image


img = Image.open('img.png')
code = pytesseract.image_to_string(img)
print(code)
