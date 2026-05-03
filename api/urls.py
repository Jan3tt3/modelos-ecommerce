from django.urls import path
from .views import ProductApiView

urlpatterns = [
    path('products/', ProductApiView.as_view(), name='products-api'),
]