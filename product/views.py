from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product


# LISTAR productos
class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'


# DETALLE de producto
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = "Detalle del producto"
        return context


# ELIMINAR producto
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/confirm_delete.html'
    success_url = reverse_lazy('product_list')

