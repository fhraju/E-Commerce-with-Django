from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product

# Create your views here.
class PrdouctListView(ListView):
    queryset = Product.objects.all()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()