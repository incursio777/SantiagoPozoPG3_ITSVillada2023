from django.urls import path
from . import views
from .views import signup, HorarioClase

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login_view),
    path('signup/', views.signup),
    path('home/', views.home, name='home'),
    path('historial/', views.historial),
    path('horario/', views.horario),
    path('inscribir/', views.inscribir),
    path('notas/', views.notas),
    path('horarios/', HorarioClase, name='horarios_clases'),
]
