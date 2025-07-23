from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


# Create your views here.

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


