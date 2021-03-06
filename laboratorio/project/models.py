from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

# Create your models here.


class Examenes(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    addres = models.CharField(verbose_name='Direccion', max_length=100)
    phone = models.CharField(verbose_name='Telefono', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    os_choice =(
        ('Cuadro Hemático', 'Cuadro Hemático'),
        ('Uroanálisis', 'Uroanálisis'),
        ('Coprológico', 'Coprológico'),
        ('Sangre oculta en materia fecal', 'Sangre oculta en materia fecal'),
        ('Colesterol Total', 'Colesterol Total'),
        ('Colesterol HDL (Bueno)', 'Colesterol HDL (Bueno)'),
        ('Colesterol LDL (Malo)', 'Colesterol LDL (Malo)'),
        ('Trigliceridos', 'Trigliceridos'),
        ('Glicemia', 'Glicemia'),
        ('Creatinina', 'Creatinina'),
        ('Nitrógeno ureico', 'Nitrógeno ureico'),
        ('Ácido úrico', 'Ácido úrico'),
        ('Transaminasa Oxalacética (TGO)', 'Transaminasa Oxalacética (TGO)'),
        ('Transaminasa Pirúvica (TGP)', 'Transaminasa Pirúvica (TGP)'),
        ('Gama Glutamil Transferasa (GGT)', 'Gama Glutamil Transferasa (GGT)'),
        ('Fosfatasa Alcalina', 'Fosfatasa Alcalina'),
        ('Proteínas diferenciadasx', 'Proteínas diferenciadasx'),
        ('Serología', 'Serología'),
        ('Hormona estimulante de la tiroides (TSH)', 'Hormona estimulante de la tiroides (TSH)'),
        ('Prueba de embarazo', 'Prueba de embarazo'),
    )
    exam = models.CharField(verbose_name='Tipo de examen', max_length=200, choices=os_choice)
    id = models.IntegerField(primary_key=True, verbose_name='Cedula')
    image = models.ImageField(verbose_name='Orden', upload_to="examenes", blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, )

    class Meta:
        verbose_name="Examen"
        verbose_name_plural="Examenes"


    def __str__(self):
        return str(self.id)

#compruea que si el modelo ha sido guardado ejecuta el signal y activa la funcion de enviar mail
# esto solo muestra el signal de que ha habido una actualizacion al admin es decir alguien ha puesto algo en da DB
@receiver(post_save, sender=Examenes)
def examenes_save(sender, instance, **kwargs):
    if kwargs['created']:
        send_mail(
            'MEDICOM',
            '''Hay un nuevo pedido de examen medico.
             El usuario: %s,    Direccion: %s       Telefono: %s
             Email: %s
             Tipo de examen: %s             Identificación: %s''' %(instance.name, instance.addres, instance.phone, instance.email, instance.exam, instance.id),
            'forexample@gmail.com', #de quien viene el mensaje
            ['saludmedicom@gmail.com'],
            fail_silently=False,
        )
