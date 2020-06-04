from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User ## esta importacion contiene todos los usuarios registrados en nuestro panel administrador y se usa para enlazar el autor del models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")



    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering = ['-created']


    def __str__(self):
        return self.name


class Publi(models.Model):
    title = models.CharField(max_length= 200, verbose_name="titulo")
    content = models.TextField(verbose_name="contenido")
    published = models.DateTimeField(verbose_name="Fecha depublicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="categorias")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        ordering = ['-created']
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.title