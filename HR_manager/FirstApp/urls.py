from django.urls import path
from FirstApp import views
from .models import *
from .views import *
from . import views




urlpatterns = [

    path('', views.access, name="logueo"),
    path('close/', views.close, name="salir"),
    path('register/', views.register, name="registro de usuario"),
    path('home/', views.home, name="Principal"),
    path('create/hoja1/', views.createHoja1, name="crea legajo base"),
    path('read/hoja1/', views.readHoja1, name="lee legajo base"),
    path('FirstApp/detail/<int:id>/', views.detailHoja1, name='CheckData'),
    path('eraseH1/', views.eraseH1, name="borrarBase"),
    path('libro-de-reclamos/', views.libro_de_reclamos, name='libro_de_reclamos'),
    path('biografia/', views.biografia, name='biografia'),
    path('ver_tablas/', views.ver_tablas, name='ver_tablas'),
    path('editar_registro/<int:registro_id>/', views.editar_registro_hoja2, name='editar_registro'),
    path('editar_registro/<int:registro_id>/', views.editar_registro_capacitacion, name='editar_registro'),
    path('nuevo_registro/hoja2/', views.nuevo_registro_hoja2, name='nuevo_registro_hoja2'),
    path('nuevo_registro/capacitacion/', views.nuevo_registro_capacitacion, name='nuevo_registro_capacitacion'),
]
