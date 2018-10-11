from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import (Vendedor,Oficina,Cliente,Panel,Inversor,Tarifa,Propuesta)
from .serializers import (VendedorSerializer,OficinaSerializer,ClienteSerializer,PanelSerializer,InversorSerializer,TarifaSerializer,PropuestaSerializer)
# Create your views here.

def indx(request):
  html="<html><head><title>noting to do here</title></head><body><h1 align='center'>Solem ApiRest</h1></body></html>"
  return HttpResponse(html)

class VendViewset(viewsets.ModelViewSet):
  queryset=Vendedor.objects.all()
  serializer_class=VendedorSerializer

class OfiViewset(viewsets.ModelViewSet):
  queryset=Oficina.objects.all()
  serializer_class=OficinaSerializer

class ClientViewset(viewsets.ModelViewSet):
  queryset=Cliente.objects.all()
  serializer_class=ClienteSerializer

class PanelViewset(viewsets.ModelViewSet):
  queryset=Panel.objects.all()
  serializer_class=PanelSerializer

class InversorViewset(viewsets.ModelViewSet):
  queryset=Inversor.objects.all()
  serializer_class=InversorSerializer

class TarifaViewset(viewsets.ModelViewSet):
  queryset=Tarifa.objects.all()
  serializer_class=TarifaSerializer

class PropuestaViewset(viewsets.ModelViewSet):
  queryset=Propuesta.objects.all()
  serializer_class=PropuestaSerializer
