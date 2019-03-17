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
    image = cv2.imread("docs/"+image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Image", gray)

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
    # print(text)

    # Data identification
    #Cedula
 
    try:
        numero = ''
        apellido = ''
        nombre = ''
        last_char = ''
        state = ''
        ape = False

        for char in text:

            if char.isdigit():
                numero = numero + char
                last_char = char
            
            if char=='\n' and last_char.isdigit():
                state = 'apellido'
            
            if state is 'apellido' and char is not '\n':
                apellido = apellido + char
                ape = True
            
            if state is 'apellido' and ape and char is '\n':
                break

        vals = text.split(apellido)[1]

        values = vals.split('\n')

        aux = 1000
        for value in values:
            # try:
            #     if value[0] is 'A' and value[1] is 'P':
            #         pass
            #     elif len(value) <2:
            #         pass
            #     elif len(value.split(' ')) >2:
            #         pass
            #     else:
            #         nombre = value
            # except:
            #     pass
            spec = len(value.split(' '))
            if spec < aux and len(value) > 5 and value[1] is not 'P' and value[0] is not 'N':
                nombre = value
                aux = spec

    except:
        numero="No determinado"
        apellido="No determinado"
        nombre="No determinado"
        
    print(numero)
    print(apellido)
    print(nombre)

    return vals,values,numero,apellido,nombre
    # show the output images
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)



