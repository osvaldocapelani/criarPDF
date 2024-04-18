from django.urls import path, include
from .views import home, gerar_certificado

urlpatterns = [
    path('', home, name="home.html"),
    path('gerar-certificado/', gerar_certificado, name='gerar_certificado'),
]
