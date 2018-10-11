from rest_framework import serializers
from .models import (Vendedor,Oficina,Cliente,Panel,Inversor,Tarifa,Propuesta)


class VendedorSerializer(serializers.ModelSerializer):
  class Meta:
    model=Vendedor
    fields=('nombre','apellido','telefono','oficina','email')

class OficinaSerializer(serializers.ModelSerializer):
  class Meta:
    model=Oficina
    fields=('ciudad','estado')

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model=Cliente
    fields=('nombre','apellido','estado','ciudad','municipio','cp','telefono','cel','email')

class PanelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Panel
    fields=('nombre','marca','potencia','isc','voc','precio','vmp')

class InversorSerializer(serializers.ModelSerializer):
  class Meta:
    model=Inversor
    fields=('nombre','potencia','precio','marca','vmin','vmax','pmin','pmax','isc')

class TarifaSerializer(serializers.ModelSerializer):
  class Meta:
    model=Tarifa
    fields=('nombre','nivel','verano','rango','precio')

class PropuestaSerializer(serializers.ModelSerializer):
  class Meta:
    model=Propuesta
    fields=('cliente','tarifa','panel','inversor','vendedor','porcentaje','potencia','rpu','consumos','fecha','potenciaABS')
