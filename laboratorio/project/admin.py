from django.contrib import admin
from .models import Examenes
from .forms import ExamForm



# Register your models here.

class ExamenesAdmin(admin.ModelAdmin):
    form = ExamForm

    list_display = ('name', 'addres', 'phone', 'email', 'id', 'image', 'exam')
    list_filter = ('exam', )
    date_hierarchy = 'created'




admin.site.register(Examenes, ExamenesAdmin)

##el admin crea el administrador de esta app en django
##list_display permite visualizar los fields en el admin
## list_filter crea una lista que es parecida como en el blog a categorias para organizar el tipo de examenes en la BD
## date_hierarchy permite organizar por fechas que los datos han entradado en BD

