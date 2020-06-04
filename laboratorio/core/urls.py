
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('exam_profile/', views.exam_profile, name='exam_profile'),
    path('exam_requeriments/', views.exam_requeriments, name='exam_requeriments'),

]
