import uuid

from django.db import models

# Create your models here.


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    order_number = models.IntegerField(null=True)
    user = models.ForeignKey("users.User", related_name="orders", on_delete=models.CASCADE)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = Order.objects.order_by("-order_number").first().order_number + 1
        super().save(*args, **kwargs)


class OrderProduct(models.Model):
    class Meta:
        verbose_name = "Order Product"
        verbose_name_plural = "Orders Products"

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    order = models.ForeignKey("orders.Order", related_name="products", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", related_name="orders", on_delete=models.CASCADE)
    qty = models.IntegerField()
