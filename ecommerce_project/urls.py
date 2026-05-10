from django.contrib import admin
from django.urls import path, include

from order_manager.views import SalesChartView, sales_dashboard

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('order_manager.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('addresses/', include('address.urls')),

    path(
        'sales-chart/',
        SalesChartView.as_view(),
        name='sales-chart'
    ),

    path(
        'sales-dashboard/',
        sales_dashboard,
        name='sales-dashboard'
    ),

    path('', include('forms_test.urls')),

    path('api/v1/', include('api.urls')),

    # JWT
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # Perfil usuario
    path(
        'api/',
        include('forms_test.urls')
    ),
]