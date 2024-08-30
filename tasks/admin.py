from django.contrib import admin
from .models import Taks
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)#readonly_fields le estamos diciendo que campos son de solo lectura y que quiero ver en pantalla , basicamente convierte el atribuo seleccionado en una tupla!

admin.site.register(Taks,TaskAdmin)