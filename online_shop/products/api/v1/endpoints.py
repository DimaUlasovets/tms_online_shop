from django.shortcuts import get_object_or_404
from products.api.v1.serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductSerializer,
)
from products.models import Brand, Category, Product
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductList(APIView):
    """
    List all products.
    """

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Single product by id
    """

    def get_single_product(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk, format=None):
        product = self.get_single_product(pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        product = self.get_single_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        product = self.get_single_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_single_product(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """
    List all Categorys.
    """

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Single category by id
    """

    def get_single_category(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, pk, format=None):
        category = self.get_single_category(pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        category = self.get_single_category(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        category = self.get_single_category(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_single_category(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandList(APIView):
    """
    List all Brands.
    """

    def get(self, request, format=None):
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetail(APIView):
    """
    Single brand by id
    """

    def get_single_brand(self, pk):
        return get_object_or_404(Brand, pk=pk)

    def get(self, request, pk, format=None):
        brand = self.get_single_brand(pk)
        serializer = BrandSerializer(brand, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        brand = self.get_single_brand(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        brand = self.get_single_brand(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_single_brand(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
