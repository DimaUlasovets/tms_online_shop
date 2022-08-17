from products.models import Brand, Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret["brend"] = BrandSerializer(obj.brend).data
        ret["category"] = CategorySerializer(obj.category).data
        return ret

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "count_stock",
            "brend",
            "category",
        ]
