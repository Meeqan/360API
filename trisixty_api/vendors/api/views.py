from vendors.models import Vendor
from utils.base_viewset import BaseViewSet
from .serializers import VendorSerializer


class VendorViewSet(BaseViewSet):
    """Vendor View set"""

    model_class = Vendor
    serializer_class = VendorSerializer
