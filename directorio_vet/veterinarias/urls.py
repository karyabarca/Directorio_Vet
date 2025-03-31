from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('veterinarias/', views.lista_veterinarias, name='lista_veterinarias'),
    path('veterinarias/<int:pk>/', views.detalle_veterinaria, name='detalle_veterinaria'),
    path('veterinarias/nueva/', views.crear_veterinaria, name='crear_veterinaria'),
    path('veterinarias/<int:pk>/editar/', views.editar_veterinaria, name='editar_veterinaria'),
    path('veterinarias/<int:pk>/eliminar/', views.eliminar_veterinaria, name='eliminar_veterinaria'),
]
