from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.encoding import smart_str
from webapp.models import *
# from series.models import Serie
# from series.serializers import SerieSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def get_landing(request):
    # return render(request, 'webapp/landing.html', {})
    if request.method == 'GET':
        return render(request, 'webapp/landing.html', {})
    else:
        return HttpResponseBadRequest(content='Error:')

@csrf_exempt
def check_code(request,input_code):
    print("Entroooo")
    try:
        if request.method == 'GET':
            print(input_code)
            query = VehicleSell.objects.get(code=input_code)
            existing_code = query.code
            print(existing_code)
            if input_code == existing_code:
                state = CodeState.objects.get(value='checked')
                query.state = state
                query.save()
                #return render(request, 'webapp/tramitSuccess.html', {})

                response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
                response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("traspaso.jpg")
                response['X-Sendfile'] = smart_str('/webapp/output/')
                # It's usually a good idea to set the 'Content-Length' header too.
                # You can also set any other required headers: Cache-Control, etc.
                return response

    except VehicleSell.DoesNotExist:
        return render(request, 'webapp/tramitFailure.html', {})

@csrf_exempt
def file_down(request):

    response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("A8299B98AAF2C5FCD66F150704D6B9A2.txt")
    response['X-Sendfile'] = smart_str('/test_files/')
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response

@csrf_exempt
def get_ssl(request):
    return HttpResponse("044DA86F7ED5800896FCA82B7A3BCC5A0326028E7CDDEBED5717D9FC8CA227F4 comodoca.com 5c8db1f10b353")





###################################################################
# Ejemplo de request/response con JSON usando djangorestframework
# @csrf_exempt
# def serie_list(request):
#     """
#     List all code serie, or create a new serie.
#     """
#     if request.method == 'GET':
#         series = Serie.objects.all()
#         serializer = SerieSerializer(series, many=True)
#         return JSONResponse(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SerieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def serie_detail(request, pk):
#     """
#     Retrieve, update or delete a serie.
#     """
#     try:
#         serie = Serie.objects.get(pk=pk)
#     except Serie.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SerieSerializer(serie)
#         return JSONResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SerieSerializer(serie, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         serie.delete()
#         return HttpResponse(status=204)