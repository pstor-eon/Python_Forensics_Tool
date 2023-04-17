import cv2
import pytesseract
from tkinter import Tk, filedialog

def main():
    Tk().withdraw()

    file_path = filedialog.askopenfilename(title="OCR할 이미지 파일 선택", filetypes=(("PNG 파일", "*.png"), ("JPEG 파일", "*.jpg"), ("모든 파일", "*.*")))

    if not file_path:
        print("파일이 선택되지 않았습니다.")
        return
      
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, lang="kor+eng")
    print("인식된 텍스트:")
    print(text)

if __name__ == "__main__":
    main()
