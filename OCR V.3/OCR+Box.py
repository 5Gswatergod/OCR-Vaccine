import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imgPath = cv2.imread(r"C:\Users\linsh\Desktop\py\image\test 2.jpg")
img = cv2.cvtColor(imgPath,cv2.COLOR_BGR2RGB)


## Detecting Words
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img, lang="chi_tra")
text = pytesseract.image_to_string(img, lang="chi_tra")
for x,b in enumerate(boxes.splitlines()):
    if x!=0:    
        b = b.split()
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(50,50,255),1)

if "AZ" in text:
    print('Found')
else:
    print('Not Found')

print(text)

cv2.imshow('Result', img)
cv2.waitKey(0)