from django.contrib import admin
from .models import Service

# Register your models here.
# Se hace la importacion del modelo que se hizo en services/models para que
# sea visible en el panel admin del navegador

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    ##determinamos que esos dos campos en los modelos solo seran de lectura y no seran
    # editables en el panel de administrador#

admin.site.register(Service, ServiceAdmin)
    ## aca se registra el modelo de Service y la configuracion que hemos creado