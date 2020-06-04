
from django.urls import path, include
from . import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
]
