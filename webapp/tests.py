from django.test import TestCase

def text_extraction(filename):
    try:
        from PIL import Image
    except ImportError:
        import Image
    import pytesseract

    # If you don't have tesseract executable in your PATH, include the following:
    # pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Simple image to string
    print(pytesseract.image_to_string(Image.open("test_tramit_files/"+filename)))



