from cotizador.views import (VendViewset,OfiViewset,ClientViewset,PanelViewset,InversorViewset,TarifaViewset,PropuestaViewset)
from rest_framework import routers

router=routers.DefaultRouter()
router.register('vendedores',VendViewset)
router.register('clientes',ClientViewset)
router.register('paneles',PanelViewset)
router.register('oficinas',OfiViewset)
router.register('inversores',InversorViewset)
router.register('tarifas',TarifaViewset)
router.register('propuestas',PropuestaViewset)
