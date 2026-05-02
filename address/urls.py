from django.urls import path
from .views import (
    AddressListView, AddressDetailView,
    AddressCreateView, AddressUpdateView, AddressDeleteView
)

urlpatterns = [
    path('', AddressListView.as_view(), name='address_list'),
    path('new/', AddressCreateView.as_view(), name='address_create'),
    path('<int:pk>/', AddressDetailView.as_view(), name='address_detail'),
    path('<int:pk>/edit/', AddressUpdateView.as_view(), name='address_update'),
    path('<int:pk>/delete/', AddressDeleteView.as_view(), name='address_delete'),
]