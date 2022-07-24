from django.urls import path
from orders.api.v1.endpoints import carts, orders
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("carts/", carts.CartAPIView.as_view(), name="carts_api"),
    path("orders/", orders.OrderAPIView.as_view(), name="orders_api"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
