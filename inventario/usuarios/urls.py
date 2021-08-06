from django.contrib import admin
from django.urls import path,include
from . import views

app_name='usuarios'
urlpatterns = [
    path('autores/',views.autores,name='autores'),
    path('autoresForm/',views.autoresForm,name='autoresForm'),
    path('autorEdit/<int:id>',views.autorEdit,name='autorEdit'),
    path('autorDelete/<int:id>',views.autorDelete,name='autorDelete'),

    #CRUD para Libros

    path('libros/',views.libros,name='libros'),
    path('libroForm/',views.libroForm,name='libroForm'),
    path('libroEdit/<int:id>',views.libroEdit,name='libroEdit'),
    path('libroDelete/<int:id>',views.libroDelete,name='libroDelete'),
]
