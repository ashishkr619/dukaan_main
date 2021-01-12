from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import ProductSerializer, StoreListSerializer, ProductCreateSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset to Manage Dukaan Store Products.
    """

    queryset = Product.objects.select_related('store')
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get_queryset(self):
        """
        Optionally restricts the products,
        by filtering against a `category` query parameter in the URL.
        """
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    # Remove CSRF request verification for posts to this API
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ProductViewSet, self).dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        store_link = self.request.query_params.get('store_link', None)
        serializer_context = {'store_link': store_link}
        queryset = queryset.filter(store__store_link=store_link)
        serializer = StoreListSerializer(queryset, many=True, context=serializer_context)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        """
        Soft deletes or deactivates a Dukaan Store.
        """
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
