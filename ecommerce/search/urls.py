from django.urls import path

from .views import PrdouctSearchView

urlpatterns = [
    path('', PrdouctSearchView.as_view(), name='search'),
]