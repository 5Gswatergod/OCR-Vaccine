import pytesseract
from PIL import Image

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(r"C:\Users\linsh\Desktop\py\pictures\slide (30).JPG")
    #img.show()
    print(pytesseract.image_to_string(img, lang="chi_tra+eng"))


if __name__ == "__main__":
    main()