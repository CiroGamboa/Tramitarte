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

def text_preproc(image, preproc="thresh"):
    # import the necessary packages
    from PIL import Image
    import pytesseract
    # import argparse
    import cv2
    import os

    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "images/example_01.png ", required=True,
    #     help="path to input image to be OCR'd")
    # ap.add_argument("-p", "--preprocess", type=str, default="thresh",
    #     help="type of preprocessing to be done")
    # args = vars(ap.parse_args())

    # load the example image and convert it to grayscale
    image = cv2.imread("images/"+image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", gray)

    # check to see if we should apply thresholding to preprocess the
    # image
    if preproc == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif preproc == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    # show the output images
    # cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)



