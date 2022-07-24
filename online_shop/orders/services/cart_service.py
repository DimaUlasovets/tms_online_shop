from functools import reduce

from django.core.cache import cache
from products.models import Product


class CartService:
    def __init__(self, user) -> None:
        self.user = user
        self.cart = self.get_user_cart()

    def add_product(self, product_data: dict):
        product: Product = Product.objects.get(id=product_data["product"])

        data_to_insert = {
            "id_product": product.id,
            "name": product.name,
            "price": product.price,
            "qty": product_data["qty"],
        }
        self.cart["products"].append(data_to_insert)
        self.cart["products_count"] = self.get_items_count_cart()
        self.cart["total_price"] = self.get_total_price()

        cache.set(self.user.id, self.cart, timeout=86400)  # 24 hours = 86400 seconds

    def get_user_cart(self):
        cart = cache.get(self.user.id)
        return cart if cart else {"products": [], "products_count": 0}

    def get_total_price(self):

        products_cart = self.cart["products"]
        total_price = reduce(
            lambda total_sum, current_item: total_sum + (current_item["price"] * current_item["qty"]), products_cart, 0
        )

        return total_price

    def get_items_count_cart(self):

        products_cart = self.cart["products"]

        cart_items_count = reduce(lambda total_count, current_item: total_count + current_item["qty"], products_cart, 0)

        return cart_items_count

    def cleare_cart(self):
        cache.delete(self.user.id)
