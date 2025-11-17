from pdf2image import convert_from_path
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
poppler_path = r"C:\Program Files\poppler-25.07.0\Library\bin"

# Add Poppler to PATH at runtime
os.environ["PATH"] += os.pathsep + poppler_path

def ocr_pdf(pdf_path, start_page=25, end_page=608):
    text = ""
    # Convert only the required page range to images
    images = convert_from_path(pdf_path, first_page=start_page, last_page=end_page)
    for i, image in enumerate(images, start=start_page):
        page_text = pytesseract.image_to_string(image, lang='eng')
        text += f"\n--- Page {i} ---\n" + page_text
        print(f"Processed page {i}")
    return text

pdf_path = "Vol2.pdf"
text = ocr_pdf(pdf_path)

text_file_path = "extracted_text.txt"
with open(text_file_path, "w", encoding="utf-8") as text_file:
    text_file.write(text)