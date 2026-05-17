import random
import string

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from cart.models import Cart
from address.models import Address


class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    order_id = models.CharField(
        max_length=120,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order {self.order_id}"

    def get_absolute_url(self):
        return f"/orders/{self.id}/"

    def get_status(self):
        return self.get_status_display()

    def calculate_total(self):

        total = sum(
            item.product.price * item.quantity
            for item in self.cart.items.all()
        )

        self.total = total

        self.save()


def generate_order_id():

    return ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=10
        )
    )


def pre_save_order_receiver(
    sender,
    instance,
    *args,
    **kwargs
):

    if not instance.order_id:

        instance.order_id = generate_order_id()


pre_save.connect(
    pre_save_order_receiver,
    sender=Order
)