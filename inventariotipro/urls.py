from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('panel/', panel, name="panel"),
    path('asignacion/', asignacion, name=" asignacion"),
    path('modificarasignacion/<id>/', modificarasignacion, name='modificarasignacion'),
    path('eliminarasignacion/<id>/', eliminarasignacion, name='eliminarasignacion'),
    path('equipos/', equipos, name="equipos"),
    path('monitores/', monitores, name="monitores"),
    path('perifericos/', perifericos, name="perifericos"),
    path('listarequipos/', listarequipos, name="listarequipos"),
    path('listarmonitores/', listarmonitores, name="listarmonitores"),
    path('listarperifericos/', listarperifericos, name="listarperifericos"),
    path('eliminarequipos/<id>/', eliminarequipos, name='eliminarequipos'),
    path('modificarmonitores/<id>/', modificarmonitores, name='modificarmonitores'),
    path('eliminarmonitores/<id>/', eliminarmonitores, name='eliminarmonitores'),
    path('modificarequipos/<id>/', modificarequipos, name='modificarequipos'),
    path('modificarperiferico/<id>/', modificarperiferico, name='modificarperiferico'),
    path('eliminarperifericos/<id>/', eliminarperifericos, name='eliminarperifericos'),
    path('registro/', registro, name='registro'),

]