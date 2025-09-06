import os
from Image_extraction import extract_text_from_image
from Pdf_extraction import extract_text_from_pdf


def process_document(file_path):
    """
    Determines file type (PDF or Image) and extracts text accordingly.
    """
    if not os.path.exists(file_path):
        print(" Error: File does not exist.")
        return

    # Get file extension
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        extract_text_from_pdf(file_path)
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        extract_text_from_image(file_path)
    else:
        print(" Unsupported file format. Please provide a PDF or image.")



