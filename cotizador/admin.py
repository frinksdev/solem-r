from django.contrib import admin
from .models import (Vendedor,Cliente,Panel,Inversor,
Oficina,Tarifa,Propuesta)

from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header='eTesla administrador'

admin.site.unregister(Group)

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Panel)
admin.site.register(Inversor)
admin.site.register(Oficina)
admin.site.register(Tarifa)
admin.site.register(Propuesta)
