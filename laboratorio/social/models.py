from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique = True)# el SlugField nos permite utilizar caracteres especiles como barras pero no espacios
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace de la red social", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add='True', verbose_name="Fecha de creacion")
    updated =  models.DateTimeField(auto_now='True', verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['name']


    def __str__(self):
        return self.name
