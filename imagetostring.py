import cv2
import numpy as np
import pytesseract
from PIL import Image

def tesseract():

    config = ('-l kor+eng')

    original_image = cv2.imread('korean.jpg')

    edge = cv2.Canny(original_image, 30, 110)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    img = Image.fromarray(original_image)

    ocr = pytesseract.image_to_string(img, lang = 'kor') #pytesseract로 문장 가져오기
    print(ocr)

tesseract()