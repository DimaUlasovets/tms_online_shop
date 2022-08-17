from django.core.cache import cache
from orders.models import Order, OrderProduct
from orders.serializers import CreateOrderSerializer, OrderSerializer
from orders.services.order_service import OrderService
from products.paginations import PaginationHandlerMixin
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView


class BasicPagination(PageNumberPagination):
    page_size_query_param = "limit"


class OrderAPIView(APIView, PaginationHandlerMixin):

    pagination_class = BasicPagination

    def get(self, request, format=None, *args, **kwargs):

        user = request.user
        order_service = OrderService(user)
        orders = order_service.get_orders()
        page = self.paginate_queryset(orders)

        if page is not None:
            serializer = self.get_paginated_response(OrderSerializer(page, many=True).data)
        else:
            serializer = OrderSerializer(orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        user = request.user
        order_service = OrderService(user)

        order = order_service.create_order()
        order_service.create_order_products(order)

        return Response(data=order.total_price, status=status.HTTP_201_CREATED)
