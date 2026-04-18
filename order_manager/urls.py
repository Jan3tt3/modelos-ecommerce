from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order),
    path('<int:id>/', views.order_detail, name='order_detail'),
]