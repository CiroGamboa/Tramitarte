from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from series.models import Serie
# from series.serializers import SerieSerializer
from webapp.models import File, CodeState, DoubleCheck

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
    print("Codigo recibido")
    try:
        if request.method == 'GET':
            print(input_code)
            new_code = DoubleCheck.objects.create(
                code = input_code, 
                state = CodeState.objects.get(value='generated'), 
                fileid = File.objects.get(id=1)
            )
        return HttpResponse(status=200)

    except DoubleCheck.DoesNotExist:
        return HttpResponse(status=400)

@csrf_exempt
def get_doc(request):
    return render(request, 'botapp/doc.html', {})

    


    return render(request, 'webapp/tramit.html', {})
