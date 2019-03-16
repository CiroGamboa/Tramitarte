from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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
def getLanding(request):
    return render(request, 'webapp/landing.html', {})
    # if request.method == 'GET':
    #     return render(request, 'webapp/landing.html', {})
    # else:
    #     return HttpResponseBadRequest(content='Error:')

@csrf_exempt
def check_code(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'webapp/tramit.html', {})





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