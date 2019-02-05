from vendors.api.views import VendorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, base_name='vendors')
urlpatterns = router.urls
