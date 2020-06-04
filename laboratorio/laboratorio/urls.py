"""laboratorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [

    #paths del la app core
    path('', include('core.urls')),


    #paths del la app services
    path('services/', include('services.urls')),


    #paths del la app blog
    path('blog/', include('blog.urls')),

    # paths del la app users
    path('users/', include('users.urls')),


    #paths del la app contact
    path('contact/', include('contact.urls')),

    #paths del la app project
    path('project/', include('project.urls')),


    #path del admin
    path('admin/', admin.site.urls),
]


## el if DICE: mientras el DEBUG del laboratorio/admin este en funcionamient oo en True se buscaran los archivos media
# ya desplegado el proyecot en la web buscand la ruta al conf. y del config a la carpeta en la raiz del proyecto

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)