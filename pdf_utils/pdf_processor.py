"""
pdf_processor.py
Handles PDF text extraction using pypdf.
"""

from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Takes a PDF file and returns the extracted text.
    Returns an empty string if extraction fails.
    """

    try:
        reader = PdfReader(uploaded_file)

        full_text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                full_text += page_text + "\n"

        return clean_text(full_text)

    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return ""


def clean_text(text):
    """
    Removes unnecessary blank lines and extra spaces.
    """

    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]

    return "\n".join(lines)


def get_page_count(uploaded_file):
    """
    Returns the number of pages in a PDF.
    """

    try:
        reader = PdfReader(uploaded_file)
        return len(reader.pages)

    except Exception:
        return 0
