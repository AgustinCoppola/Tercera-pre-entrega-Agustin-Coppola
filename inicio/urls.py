from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('djusers/crear/', views.crear_djuser, name='crear_djuser')
]