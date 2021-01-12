from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer, OrderSerializer
from .models import Cart, Order
from products.models import Product
from accounts.models import Account

"""
people (Un-authenticated users) can add items into their cart.

Maintain a cart on the server in either DB or redis or MongoDb
On cart change (add / remove item) update the cart on server
For cart line items take product id, qty, storeLink as input and fetch product meta data from the DB and save them.
---->
We can achieve this by setting a cookie containing the cart data.
https://stackoverflow.com/questions/39826992/how-can-i-set-a-cookie-in-react
We'll not need any backend for this as this can be build with javascript.
"""


class GetCartDetail(RetrieveAPIView):
    """ Retrieve Cart Detail"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'user'
    permission_classes = (IsAuthenticated,)


class AddToCartView(APIView):
    """ Add item to CArt """

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id', None)
        quantity = request.data.get('quantity')
        user_id = request.data.get('user_id', None)

        if product_id is None:
            return Response({"message": "Invalid product id"}, status=HTTP_400_BAD_REQUEST)

        if user_id is None:
            return Response({"message": "Invalid user"}, status=HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(Account, id=user_id)
        cart = get_object_or_404(Cart, user=user)
        cart.quantity = int(quantity)
        cart.product = product
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class RemoveFromCartView(APIView):
    """ Remove item from Cart """

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id', None)
        quantity = request.data.get('quantity')
        user_id = request.data.get('user_id', None)

        if product_id is None:
            return Response({"message": "Invalid product id"}, status=HTTP_400_BAD_REQUEST)

        if user_id is None:
            return Response({"message": "Invalid user"}, status=HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(Account, id=user_id)
        cart = get_object_or_404(Cart, user=user)
        cart.quantity = int(quantity)
        cart.product = product
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class ClearCartView(APIView):
    """ Clear product and quantity from Cart """

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id', None)
        if user_id is None:
            return Response({"message": "Invalid user"}, status=HTTP_400_BAD_REQUEST)
        user = get_object_or_404(Account, id=user_id)
        cart = get_object_or_404(Cart, user=user)
        cart.quantity = 0
        cart.product = None
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    """
    Lets User Create an order .
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Remove CSRF request verification for posts to this API
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(OrderViewSet, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
