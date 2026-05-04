from rest_framework.routers import DefaultRouter

from .views import (
    CartViewSet,
    ProductViewSet,
    OrderViewSet,
    AddressViewSet,
    BillingViewSet,
)

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'billings', BillingViewSet)

urlpatterns = router.urls