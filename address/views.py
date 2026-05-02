from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Address


# 📋 LISTAR direcciones del usuario
class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'address/list.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        # Solo direcciones del usuario logueado
        return Address.objects.filter(user=self.request.user)


# 🔍 DETALLE de dirección
class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'address/detail.html'
    context_object_name = 'address'


# ➕ CREAR dirección
class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    template_name = 'address/form.html'
    fields = ['street', 'city', 'state', 'country', 'postal_code']
    success_url = reverse_lazy('address_list')

    def form_valid(self, form):
        # Asignar usuario automáticamente
        form.instance.user = self.request.user
        return super().form_valid(form)


# ✏️ EDITAR dirección
class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    template_name = 'address/form.html'
    fields = ['street', 'city', 'state', 'country', 'postal_code']
    success_url = reverse_lazy('address_list')


# 🗑️ ELIMINAR dirección
class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'address/confirm_delete.html'
    success_url = reverse_lazy('address_list')