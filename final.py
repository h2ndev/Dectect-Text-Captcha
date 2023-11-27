import cv2
import os
import pytesseract

def filter_black(image):
    # Chỉ giữ lại màu đen và loại bỏ mọi màu khác
    _, binary_image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

    return binary_image

def detect_text(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    black_image = filter_black(image)

    # Nhận dạng chữ cái bằng pytesseract
    result = pytesseract.image_to_string(black_image, config='--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

    # In kết quả
    print(f"File: {image_path}, Recognized Text: {result.strip()}")

# Đường dẫn tệp ảnh cụ thể
image_path = "Dectect-Text-Captcha/Captcha/1.png"

detect_text(image_path)
#result "File: Dectect-Text-Captcha/Captcha/1.png, Recognized Text: 6Db4Av"