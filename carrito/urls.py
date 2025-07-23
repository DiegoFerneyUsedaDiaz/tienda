from django.urls import path
from django.views.generic import TemplateView
from carrito import views

app_name = 'carrito'
urlpatterns = [
    path('', views.index, name='index'),
]

