# Detect Text In Image

![Demo](https://imgur.com/8k1tGSq.png)

## Description

The text detection software is designed to recognize and extract characters from images. This application utilizes the OpenCV and pytesseract libraries to perform the recognition process.

## Features

- **Extract Text From Image**: Cut characters from the captcha.
- **Character Recognition**: Perform the process of recognizing characters from the image.
- **Display Results**: Display the recognized text results on the user interface.

## Requirements

- **Python >= 3.6**
- **pytesseract Library**
- **OpenCV Library**
- **Tesseract OCR**

## Testing

![Demo](https://imgur.com/w3beUpV.png)

Let's try to solve the captcha above.

- **Step 1**: Replace the `image_path` in the `final.py` file with the actual path.
- **Step 2**: Run the code and observe the result.

Result after running the code:

![Result after running the code](https://imgur.com/Vss84cR.png)

```
File: Dectect-Text-Captcha/Captcha/1.png, Recognized Text: 6Db4Av
```

So, the code successfully analyzed the captcha.
