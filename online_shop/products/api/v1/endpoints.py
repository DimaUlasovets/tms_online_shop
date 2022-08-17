from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from products.api.v1.serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductSerializer,
)
from products.models import Brand, Category, Product
from products.paginations import PaginationHandlerMixin
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BasicPagination(PageNumberPagination):
    page_size_query_param = "limit"


class ProductList(APIView, PaginationHandlerMixin):
    """
    List all products.
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None, *args, **kwargs):

        category = self.request.query_params.get("category", None)
        brend = self.request.query_params.get("title", None)

        products = Product.objects.all()

        if category:
            products = products.filter(category__name__contains=category)
        if brend:
            products = products.filter(brend__name__contains=brend)

        page = self.paginate_queryset(products)

        if page is not None:
            serializer = self.get_paginated_response(ProductSerializer(page, many=True).data)
        else:
            serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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

    permission_classes = [AllowAny]

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


class CategoryList(APIView, PaginationHandlerMixin):
    """
    List all Categorys.
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):
        category = Category.objects.all()
        page = self.paginate_queryset(category)

        if page is not None:
            serializer = self.get_paginated_response(CategorySerializer(page, many=True).data)
        else:
            serializer = CategorySerializer(category, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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

    permission_classes = [AllowAny]

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


class BrandList(APIView, PaginationHandlerMixin):
    """
    List all Brands.
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):
        brand = Brand.objects.all()
        page = self.paginate_queryset(brand)

        if page is not None:
            serializer = self.get_paginated_response(BrandSerializer(page, many=True).data)
        else:
            serializer = BrandSerializer(brand, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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

    permission_classes = [AllowAny]

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
