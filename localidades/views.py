from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Municipio

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).all()
    municipios_list = [{"id": m.id, "nombre": m.nombre} for m in municipios]
    return JsonResponse(municipios_list, safe=False)

from django.shortcuts import render
from .models import Estado

def seleccionar_estado(request):
    estados = Estado.objects.all()
    return render(request, 'seleccion_estado.html', {'estados': estados})