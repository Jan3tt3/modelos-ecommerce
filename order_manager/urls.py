from django.urls import path
from .views import SalesChartView, create_order, OrderDetailView, OrderListView, sales_dashboard

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('', OrderListView.as_view(), name='order_list'),
   
]