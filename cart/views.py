
from django.shortcuts import redirect, render
from .models import Cart
from product.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    return render(request, 'cart/detail.html', {'cart': cart})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)

    return redirect('/cart/')


@login_required
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart = Cart.objects.get(user=request.user)
    cart.products.remove(product)

    return redirect('/cart/')