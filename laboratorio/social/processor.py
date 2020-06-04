

########################################################################
## Aca se crea un diccionario de contexto que lo que hace es extender ##
## un diccionario en este caso el contexto de las redes sociales para ##
## que puedan ser vistas en cualquier template del proyecto. Estos    ##
## diccionarios quedaria como por defecto en cualquier template y no  ##
## necesidad de agragarlos uno por uno a cada template.               ##
## Se debe activar en el admin globalen la seccion deprocessor        ##
## la ruta hasta llegar a la funcion que definimmos aca abajo         ##
########################################################################


from .models import Link

def ctx_dic(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx