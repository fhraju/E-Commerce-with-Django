from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

class PrdouctSearchView(ListView):
    template_name = 'search/search_view.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()
