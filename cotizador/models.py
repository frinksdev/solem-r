from django.db import models

# Create your models here.

class Oficina(models.Model):
  ciudad=models.CharField(max_length=75)
  estado=models.CharField(max_length=75)

  def __str__(self):
    return '%s, %s'%(self.ciudad,self.estado)

class Vendedor(models.Model):
  nombre=models.CharField(max_length=70)
  apellido=models.CharField(max_length=70)
  oficina=models.ForeignKey('Oficina',on_delete=models.CASCADE)
  telefono=models.CharField(max_length=10)
  email=models.EmailField(max_length=254)
  
  def __str__(self):
    return '%s %s'%(self.nombre, self.apellido)

class Cliente(models.Model):
  nombre=models.CharField(max_length=70)
  apellido=models.CharField(max_length=70)
  estado=models.CharField(max_length=75)
  ciudad=models.CharField(max_length=75)
  municipio=models.CharField(max_length=75)
  cp=models.CharField(max_length=5)
  telefono=models.CharField(max_length=10)
  cel=models.CharField(max_length=10)
  email=models.EmailField(max_length=254)

  def __str__(self):
    return '%s %s'%(self.nombre,self.apellido)

class Panel(models.Model):
  nombre=models.CharField(max_length=80)
  marca=models.CharField(max_length=50)
  potencia=models.IntegerField()
  isc=models.FloatField()
  voc=models.FloatField()
  precio=models.FloatField()
  vmp=models.FloatField()
  
  def __str__(self):
    return self.nombre

class Inversor(models.Model):
  nombre=models.CharField(max_length=50)
  potencia=models.IntegerField()
  precio=models.FloatField()
  marca=models.CharField(max_length=50)
  vmin=models.IntegerField()
  vmax=models.IntegerField()
  pmin=models.IntegerField()
  pmax=models.IntegerField()
  isc=models.FloatField()

  def __str__(self):
    return self.nombre

class Tarifa(models.Model):
  nombre=models.CharField(max_length=50)
  nivel=models.IntegerField()
  verano=models.IntegerField()
  rango=models.IntegerField()
  precio=models.FloatField()

  def __str__(self):
    extra=''
    if self.verano==0 :
      extra='No Verano'
    else:
      extra='Verano'
    return '%s : %s'%(self.nombre,extra)

class Propuesta(models.Model):
  cliente=models.ForeignKey('Cliente',on_delete=models.CASCADE)
  tarifa=models.ForeignKey('Tarifa',on_delete=models.CASCADE)
  panel=models.ForeignKey('Panel',on_delete=models.CASCADE)
  inversor=models.ForeignKey('Inversor',on_delete=models.CASCADE)
  vendedor=models.ForeignKey('Vendedor',on_delete=models.CASCADE)
  porcentaje=models.IntegerField()
  potencia=models.IntegerField()
  rpu=models.CharField(max_length=60)
  consumos=models.CharField(max_length=25)
  fecha=models.DateTimeField(auto_now=True)
  potenciaABS=models.CharField(max_length=25)

  def __str__(self):
    return '%s @ %s'%(self.cliente,str(self.potencia))

