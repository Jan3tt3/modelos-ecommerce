from django.shortcuts import redirect
from cart.models import Cart
from .models import Order

from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    cart = Cart.objects.get(user=request.user)

    total = sum([p.price for p in cart.products.all()])

    Order.objects.create(cart=cart, total=total)

    cart.products.clear()

    return redirect('/products/')