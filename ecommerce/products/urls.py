from django.urls import path

from .views import PrdouctListView, ProductDetailSlugView

urlpatterns = [
    path('', PrdouctListView.as_view(), name='products-list'),
    path('<str:slug>/', ProductDetailSlugView.as_view(), name='products-detail'),
]