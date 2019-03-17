from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# from series.models import Serie
# from series.serializers import SerieSerializer
from webapp.models import CodeState, VehicleSell
import random
import string
from PIL import Image
import pytesseract
# import argparse
import cv2
import os


#################################################################
'''
Help classes
'''
#################################################################
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class DocProcessor():

    def extract_text(self,image,preproc="blur"):
    # import the necessary packages


        # load the example image and convert it to grayscale
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

        return text

    def process_cedula(self,text):
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

                spec = len(value.split(' '))
                if spec < aux and len(value) > 5 and value[1] is not 'P' and value[0] is not 'N':
                    nombre = value
                    aux = spec

        except:
            numero="No determinado"
            apellido="No determinado"
            nombre="No determinado"
            
        return numero,apellido,nombre

    # def process_tarjeta_propiedad(self,text):








'''
Por lo pronto el estado puede ser 'generado' (id=1)
Falta ver como asiganar el id del archivo, cuando se tengan archivos realmente
'''
@csrf_exempt
def receive_code(request,input_code):
    #This is made now in the receive_doc method

    # print("Codigo recibido")
    # try:
    #     if request.method == 'GET':
    #         print(input_code)
    #         new_code = DoubleCheck.objects.create(
    #             code = input_code, 
    #             state = CodeState.objects.get(value='generated'), 
    #             fileid = File.objects.get(id=1)
    #         )
    #     return HttpResponse(status=200)

    # except DoubleCheck.DoesNotExist:
    #     return HttpResponse(status=400)
    return HttpResponse(status=400)

@csrf_exempt
def doc_view(request):
    return render(request, 'botapp/doc.html', {})

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

def random_string(string_len=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_len))


def gen_img(numero,apellido,nombre):
    import json
    with open('/home/cirogam22/Desktop/Tramitarte/webapp/config.json') as f:
        data = json.load(f)
    ap = apellido.split(" ")
    data["propietario"]["primer_apellido"]=ap[0]
    data["propietario"]["segundo_apellido"]=ap[1]
    data["propietario"]["nombres"]=nombre
    data["propietario"]["num_doc"]=numero

    with open('/home/cirogam22/Desktop/Tramitarte/webapp/config.json', 'w') as f:
        json.dump(data,f)

    import os
    os.system("python3 /home/cirogam22/Desktop/Tramitarte/webapp/jpgProcessing\ .py")


@csrf_exempt
def receive_doc(request):
   
    '''
    It is necessary to find the way to save both files at the same time
    '''
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            last = False
            # Generate unique code
            code = random_string(6)
            pic = form.cleaned_data['image']
            state = CodeState.objects.get(id=1)


            last_sell = VehicleSell.objects.all().order_by('-id')[0]

            #### This corresponds to the scan of the vehicle property card
            # if last_sell.seller_propiedad == "images/":
            #     last_sell.seller_propiedad = pic

            # elif last_sell.buyer_cedula == "images/":
            #     last_sell.buyer_cedula = pic

            # elif last_sell.buyer_propiedad == "images/":
            #     last_sell.buyer_propiedad = pic
            #     last = True

            if last_sell.buyer_cedula == "images/":
                last_sell.buyer_cedula = pic
                last = True

            else:
                last_sell = VehicleSell.objects.create(code=code,state=state,seller_cedula=pic)
            
            last_id = last_sell.id
            if last:
                # Process images and fill format
                img_processor = DocProcessor()

                # Process seller cedula
                seller_cedula = last_sell.seller_cedula.path
                parts = seller_cedula.split('/')

                print(seller_cedula)
                results = img_processor.extract_text(seller_cedula,"blur")
                numero, apellido, nombre = img_processor.process_cedula(results)

                # JSON for writing output image
                gen_img(numero,apellido,str(nombre))
                
                print(numero)
                print(apellido)
                print(nombre)
                code = last_sell.code
                last_sell.save()
                return HttpResponse(code)
            else:
                last_sell.save()
                return render(request, 'botapp/doc.html', {})

        else:
            return HttpResponse("No se subioooo")
    else:
        return HttpResponse("Solo se puede con POST")



