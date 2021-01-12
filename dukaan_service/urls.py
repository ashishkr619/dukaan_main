"""dukaan_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import LoginAPIView
from accounts.views import RegistrationViewSet
from stores.views import StoreViewSet
from products.views import ProductViewSet
from carts.views import AddToCartView, GetCartDetail, RemoveFromCartView, ClearCartView, OrderViewSet


swagger_info = openapi.Info(
    title="Dukaan service",
    default_version='latest',
    description="A microservice for managing DUKAAN ecommerce application",
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# router configurations
router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'users', RegistrationViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'orders', OrderViewSet)
# openapi implementation

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('health_check/', include('health_check.urls')),
    # path('api/users/', RegistrationAPIView.as_view(), name='register-user'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('get-cart-detail/<int:user>/', GetCartDetail.as_view(), name='get-cart-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('clear-cart/', ClearCartView.as_view(), name='clear-cart'),





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
urlpatterns += staticfiles_urlpatterns()
