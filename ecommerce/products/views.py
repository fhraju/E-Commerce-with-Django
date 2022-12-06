from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product
from carts.models import Cart

# Create your views here.
class PrdouctListView(ListView):
    queryset = Product.objects.all()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context