from django.db import models
from address.models import Address
from django.contrib.auth.models import User

# Create your models here.

class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"Billing Profile of {self.user.username}"