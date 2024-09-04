import easyocr

img_path = r"C:\Users\linsh\Downloads\2.png"

reader = easyocr.Reader(['ch_tra'], gpu=False)
result = reader.readtext(img_path)

word = ''

for i in result:
    word += str(i[1])
    print(word)
