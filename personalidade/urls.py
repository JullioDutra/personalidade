from django.urls import path
from . import views

urlpatterns = [
    path('', views.teste_personalidade, name='teste_personalidade'),
    path('resultado/<int:participante_id>/', views.resultado_personalidade, name='resultado_personalidade'),
]
