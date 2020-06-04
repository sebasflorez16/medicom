from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ExamForm


# Create your views here.


def project(request):

    form = ExamForm()   #instanciamos el formulario

    if request.method == 'POST':    # si el method en el template es POST envia el formulario para que sea visto
        form = ExamForm(request.POST, request.FILES)        #el request.FILE permite que se carge la imagen del formulari a la BD siempre que en el template tenga enctype="multipart/form-data" como sentencia en el form

        if form.is_valid():     # se verifica si todos los datos del formulario son correctos y sigue
            instance = form.save(commit=False) # si todo ha ido bien guarda la instancia en la BD
            instance.save()
            print("Hemos recibido tu solicitud. En breve noscomunicaremos con tigo")

            return redirect(reverse('project') + "?ok" ) # al enviarse el form devuelve a la pagina donde se estaba

    return render(request, 'project/project.html', {'form':form})  #renderisa el template y pasa como formulario de contexto al formulario

