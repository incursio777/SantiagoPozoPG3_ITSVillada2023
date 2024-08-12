from django.urls import path
from .views import *

urlpatterns = [
    path('hola/', hola, name='hola'),
    path('template/', template),
]
