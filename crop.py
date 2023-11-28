import cv2
import os
import pytesseract

def filter_black(image):
    # Chỉ giữ lại màu đen và loại bỏ mọi màu khác
    _, binary_image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

    return binary_image

def detect_text(image):
    black_image = filter_black(image)

    # Nhận dạng chữ cái bằng pytesseract
    result = pytesseract.image_to_string(black_image, config='--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

    # In kết quả
    return result.strip()

def crop_and_save_characters(image_folder, output_folder):
    # Lấy danh sách tất cả các tệp ảnh trong thư mục
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Lặp qua từng tệp ảnh
    for image_file in image_files:
        # Tạo đường dẫn đầy đủ đến tệp ảnh
        image_path = os.path.join(image_folder, image_file)

        # Đọc ảnh
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Lọc chỉ giữ lại màu đen
        black_image = filter_black(image)

        # Lấy kích thước của ảnh
        height, width = black_image.shape

        # Tách từng chữ cái (giả sử có 6 chữ cái trong mỗi ảnh)
        for i in range(6):
            start_col = i * width // 6
            end_col = (i + 1) * width // 6

            # Cắt và lưu từng chữ cái vào thư mục đầu ra
            character = black_image[:, start_col:end_col]
            char_label = f"{image_file.split('.')[0]}_{i}"
            char_name = detect_text(character)

            char_folder = os.path.join(output_folder, char_name)
            if not os.path.exists(char_folder):
                os.makedirs(char_folder)

            char_image_path = os.path.join(char_folder, f"{char_label}.png")
            cv2.imwrite(char_image_path, character)

# Đường dẫn thư mục chứa ảnh
image_folder_path = "Dectect-Text-Captcha/Captcha"
output_folder = "Dectect-Text-Captcha/results"

# Sử dụng hàm để xử lý tất cả các ảnh trong thư mục
crop_and_save_characters(image_folder_path, output_folder)
