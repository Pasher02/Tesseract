import cv2
import numpy as np
import pytesseract
from PIL import Image

cap = cv2.VideoCapture(0)

def capture():
    if cap.isOpened() == False :
        print('Unable to rerad camera feed') #웹캠이 연결 안될 경우

    while True:
        ret, img = cap.read()
        if not ret:
            print("can't read camera")
            break

        cv2.imshow('PC_camera', img)
    
        if cv2.waitKey(1) == ord('c'):
            img_captured = cv2.imwrite('image_capture.png', img)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()    


def tesseract():

    config = ('-l kor+eng')

    original_image = cv2.imread('image_capture.png')

    edge = cv2.Canny(original_image, 30, 110)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    img = Image.fromarray(original_image)
    
    edge_color.show()
    ocr = pytesseract.image_to_string(img, lang = 'kor') #pytesseract로 문장 가져오기
    print(ocr)

capture()
tesseract()

