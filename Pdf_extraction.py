# filename: pdf_to_text_pypdf.py

import os
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF using pypdf and saves it to 'extracted_text.txt'
    in the current running folder. The file is overwritten each run.
    
    Args:
        pdf_path (str): Path to the input PDF file.
    """
    extracted_text = ""

    # Open the PDF file
    reader = PdfReader(pdf_path)

    # Loop through all pages and extract text
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            extracted_text += f"\n--- Page {page_num} ---\n{text}\n"

    # Save to extracted_text.txt in current folder
    output_txt_path = os.path.join(os.getcwd(), "extracted_text.txt")
    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text)

    print(f"✅ Extracted text saved to: {output_txt_path}")


# Example usage
if __name__ == "__main__":
    pdf_path = "Complain_Tejas.pdf"  # Replace with your input file
    extract_text_from_pdf(pdf_path)
