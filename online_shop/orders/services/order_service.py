from django.core.cache import cache
from orders.models import Order, OrderProduct
from orders.services.cart_service import CartService
from products.models import Product


class OrderService:
    def __init__(self, user) -> None:
        self.user = user
        self.cart_service = CartService(user)

    def create_order(self):

        order = Order.objects.create(user=self.user, total_price=self.cart_service.get_total_price())

        return order

    def create_order_products(self, order: Order):
        cart = self.cart_service.get_user_cart()

        order_products = OrderProduct.objects.bulk_create(
            [
                OrderProduct(
                    order=order,
                    product=Product.objects.get(id=i["id_product"]),
                    qty=i["qty"],
                )
                for i in cart["products"]
            ]
        )

        self.cart_service.cleare_cart()

        return order_products

    def get_orders(self):
        orders = Order.objects.filter(user=self.user)
        return orders
