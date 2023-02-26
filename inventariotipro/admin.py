from django.contrib import admin
from .models import Equipos, Monitores, Perifericos, Departamento, Asignacion
# Register your models here.

admin.site.register(Equipos)
admin.site.register(Monitores)
admin.site.register(Perifericos)
admin.site.register(Departamento)
admin.site.register(Asignacion)