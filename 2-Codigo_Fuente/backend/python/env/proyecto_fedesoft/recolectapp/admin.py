from django.contrib import admin
from .models import Usuario, Ubicacion, Localidad
#from .models import Ubicacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ubicacion)
admin.site.register(Localidad)