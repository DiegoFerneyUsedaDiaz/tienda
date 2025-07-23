from django.urls import path
from django.views.generic import TemplateView
from carrito import views

app_name = 'carrito'
urlpatterns = [
    path ('', TemplateView.as_view(template_name='index.html'), name='index'),
]

