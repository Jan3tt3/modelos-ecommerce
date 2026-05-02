from django.shortcuts import redirect
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .models import Cart
from product.models import Product


# DETALLE DEL CARRITO (CBV)
class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'cart/detail.html'
    context_object_name = 'cart'

    # No usaremos pk en URL; siempre es el carrito del usuario
    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


#  AGREGAR AL CARRITO (CBV tipo acción)
class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.products.add(product)
        return redirect('cart_detail')


# ➖ QUITAR DEL CARRITO (CBV tipo acción)
class RemoveFromCartView(LoginRequiredMixin, View):
    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            raise Http404("No existe carrito para este usuario")
        cart.products.remove(product)
        return redirect('cart_detail')