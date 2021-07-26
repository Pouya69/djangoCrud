from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, ManyToManyField
# Create your models here.


class Order(models.Model):
    CLASS_TYPES = [
        ("grocery", "Grocery"),
        ("enterprise", "Enterprise"),
    ]

    product_name = models.CharField(max_length=15)
    price = models.FloatField()
    class_type = models.CharField(max_length=20, choices=CLASS_TYPES)
    quantity = models.IntegerField(default=1)
    user = ForeignKey('UserMain', related_name="django_user", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.pk


class UserMain(models.Model):
    original_user = ForeignKey(User, related_name="django_user", on_delete=models.CASCADE, blank=False, null=False)
    orders = ManyToManyField(Order, related_name="user_orders", default=None)

    def __str__(self):
        return self.original_user.username
