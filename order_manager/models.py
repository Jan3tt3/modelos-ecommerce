import random
import string

from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from django.db.models.signals import pre_save


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    order_id = models.CharField(max_length=120, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pendiente'),
            ('completed', 'Completado'),
            ('cancelled', 'Cancelado')
        ],
        default='pending'
    )

    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id}"

    # URL de la orden
    def get_absolute_url(self):
        return f"/orders/{self.id}/"

    # Estado formateado
    def get_status(self):
        return self.get_status_display()
    
def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def pre_save_order_receiver(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = generate_order_id()


pre_save.connect(pre_save_order_receiver, sender=Order)