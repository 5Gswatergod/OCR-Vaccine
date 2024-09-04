import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open(r"C:\Users\linsh\Desktop\py\image\IMG_1468.PNG")
text = pytesseract.image_to_string(image)
print(text)