from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Cart
from order_manager.models import Order
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Order


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


# 
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = "Detalle de la orden"
        return context

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from order_manager.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        orders = self.get_queryset()

        context['recent_orders'] = orders.order_by('-created_at')[:5]
        context['paid_orders'] = orders.filter(status='completed')
        context['pending_orders'] = orders.filter(status='pending')
        context['cancelled_orders'] = orders.filter(status='cancelled')

        return context


class SalesChartView(View):

    def get(self, request, *args, **kwargs):

        sales = (
            Order.objects
            .filter(status='completed')
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(total_sales=Sum('total'))
            .order_by('month')
        )

        labels = []
        data = []

        for sale in sales:

            labels.append(
                sale['month'].strftime('%B')
            )

            data.append(
                float(sale['total_sales'])
            )

        return JsonResponse({
            'labels': labels,
            'data': data
        })
    
def sales_dashboard(request):
    return render(request, 'order_manager/chart.html')