from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_home, name='cart'),
    path('checkout/', views.checkout_home, name='checkout'),
    path('update/', views.cart_update, name='cart-update'),
]