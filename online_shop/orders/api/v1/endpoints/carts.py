from django.core.cache import cache
from django.shortcuts import get_object_or_404
from orders.serializers import CartAddProductSerializer
from orders.services.cart_service import CartService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CartAPIView(APIView):
    def get(self, request):

        cart_serivce = CartService(request.user)
        cart = cart_serivce.get_user_cart()
        return Response(data=cart, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CartAddProductSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user

            cart_serivce = CartService(user)
            cart_serivce.add_product(serializer.data)

            return Response(data=cart_serivce.get_user_cart(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        cart = CartService(request.user)
        cart.cleare_cart()
        return Response(status=status.HTTP_204_NO_CONTENT)
