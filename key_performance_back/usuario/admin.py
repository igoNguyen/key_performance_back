from django.contrib import admin
from informe.models import ReporteBase, Informe, Grafica
from registro.models import Pais

# Register your models here.


class ReporteBaseAdmin(admin.ModelAdmin):

    search_fields = ['semana','fecha_inicio','fecha_fin','creacion']
    list_display  = ('semana','fecha_inicio','fecha_fin',)

class InformeAdmin(admin.ModelAdmin):

    search_fields = ['fecha_inicio','estado']
    list_display  = ('fecha_inicio','fecha_fin','nombre','descripcion','estado',)    


admin.site.register(ReporteBase,ReporteBaseAdmin)
admin.site.register(Informe,InformeAdmin)
admin.site.register(Grafica)
admin.site.register(Pais)


