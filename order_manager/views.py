from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from order_manager.models import Order


@login_required
def create_order(request):
    cart = Cart.objects.get(user=request.user)

    existing_order = Order.objects.filter(cart=cart).first()

    if existing_order:
        return redirect(existing_order.get_absolute_url())

    total = sum([p.price for p in cart.products.all()])

    order = Order.objects.create(
        user=request.user,
        cart=cart,
        total=total
    )

    cart.products.clear()

    return redirect(order.get_absolute_url())


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'order/detail.html', {'order': order})