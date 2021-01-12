from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import StoreSerializer, StoreCreateSerializer
from .models import Store


class StoreViewSet(viewsets.ModelViewSet):
    """
    Viewset to Manage Dukaan Store.
    """

    # Display All Stores info which are  not soft deleted
    queryset = Store.objects.filter(is_deleted=False)
    serializer_class = StoreSerializer
    lookup_field = 'store_link'
    permission_classes = (AllowAny,)

    # Remove CSRF request verification for posts to this API
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(StoreViewSet, self).dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = StoreCreateSerializer(data=request.data)
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
