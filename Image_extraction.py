# filename: image_to_text.py

import os
from PIL import Image
import pytesseract

# Load tesseract (Windows path, change if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """
    Extracts text from an image using OCR (Tesseract)
    and saves it to 'extracted_text.txt' in the current folder.
    The file is overwritten each run.
    
    Args:
        image_path (str): Path to the input image (JPG, PNG, etc.)
    """
    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.open(image_path))

    # Save to text file
    output_txt_path = os.path.join(os.getcwd(), "extracted_text.txt")
    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    print(f"✅ OCR text extracted and saved to: {output_txt_path}")


# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\Lenovo\Desktop\GGENAI\image.png"  # Correct full path
    extract_text_from_image(image_path)
