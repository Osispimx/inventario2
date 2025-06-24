
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),  # ejemplo de ruta
]


# todo agregar el url y las views