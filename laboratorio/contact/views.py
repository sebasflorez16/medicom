from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()  ##esto lo que hace es instanciar o crear el objeto de form en el template como un objeto luego se pasa un diccionario de contexto

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) ## verifica si se han enviado algun dato por POST entonces rellena el formulario. y comprueba si el formulario es valido
        if contact_form.is_valid():         ## esto verifica que que todos los campos del formulario sean correcto para enviar y recupera los datos
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            site = request.POST.get('site', '')
            content = request.POST.get('content', '')
                                                            # si todo se verifica que todos los datos son correcto se redirecciona al template contact y se le indica al usuario que el mensaje ha sido enviado

            email = EmailMessage(                           # formato en el que llega el mensaje al destino y a quien llega
                "Laboratorio del llano: Nuevo mensaje",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "No-contestar@mailtrap.io",
                ["juansebastianflorezescobar@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                ## si todo ha salido bien se envia el correo
                return redirect(reverse('contact') + "?ok")

            except:
                ## si algo salio mal se reversa al FAIL
                return redirect(reverse('contact') + "?fail")         ## reversa al template contact automaticamente si todas las setencias se complen. En el html verifica esta sentencia para enviar mensaje aprovado al usuario con un if templateTag


    return render(request, 'contact/contact.html', {'form':contact_form})