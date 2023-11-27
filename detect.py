import cv2
import os
import pytesseract

def recognize_characters(image_folder):
    # Lấy danh sách tất cả các tệp ảnh trong thư mục
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Lặp qua từng tệp ảnh
    for image_file in image_files:
        # Tạo đường dẫn đầy đủ đến tệp ảnh
        image_path = os.path.join(image_folder, image_file)

        # Đọc ảnh
        image = cv2.imread(image_path)

        # Chuyển đổi ảnh sang ảnh đen trắng (nếu cần thiết)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Nhận dạng chữ cái bằng pytesseract
        result = pytesseract.image_to_string(gray_image, config='--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

        # In kết quả
        print(f"File: {image_file}, Recognized Text: {result.strip()}")

# Đường dẫn thư mục chứa ảnh
image_folder_path = "Dectect-Text-Captcha/results"

# Sử dụng hàm để nhận dạng chữ cái trong tất cả các ảnh trong thư mục
recognize_characters(image_folder_path)
