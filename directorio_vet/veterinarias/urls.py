from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.detalle_veterinaria, name='detalle_veterinaria'),
    path('nuevo/', views.crear_veterinaria, name='crear_veterinaria'),
    path('<int:pk>/editar/', views.editar_veterinaria, name='editar_veterinaria'),
    path('<int:pk>/eliminar/', views.eliminar_veterinaria, name='eliminar_veterinaria'),
]
