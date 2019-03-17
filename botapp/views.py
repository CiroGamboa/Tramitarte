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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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


@csrf_exempt
def receive_doc(request):
    '''
    It is necessary to find the way to save both files at the same time
    '''
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():


            # Generate unique code
            code = random_string(6)
            pic = form.cleaned_data['image']
            state = CodeState.objects.get(id=1)

            last_sell = VehicleSell.objects.all().order_by('-id')[0]
            if last_sell.buyer_pic == "images/":
                last_sell.buyer_pic = pic
            else:
                last_sell = VehicleSell.objects.create(code=code,state=state,seller_pic=pic)
            last_sell.save()

            return render(request, 'botapp/doc.html', {})

        else:
            return HttpResponse("No se subioooo")
    else:
        return HttpResponse("Solo se puede con POST")



