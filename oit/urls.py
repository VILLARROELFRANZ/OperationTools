from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_oits, name='listar_oits'),
    path('completadas/', views.oits_completadas, name='oits_completadas'),
    path('crear/', views.crear_oit, name='crear_oit'),
    path('detalle/<int:oit_id>/', views.detalle_oit, name='detalle_oit'),
    path('completar/<int:oit_id>/', views.completar_oit, name='completar_oit'),
    path('eliminar/<int:oit_id>/', views.eliminar_oit, name='eliminar_oit'),
    path('editar/<int:oit_id>/', views.editar_oit, name='editar_oit'),

]

