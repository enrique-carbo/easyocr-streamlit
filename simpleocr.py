import easyocr as ocr  #OCR

reader = ocr.Reader(['en'], gpu = False)

result = reader.readtext("english-ocr.png")

for text in result:
    print(text[1])