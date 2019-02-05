from django.db import models
from utils.auditable_model import AuditableModel
from users.models import User


class Vendor(AuditableModel):
    """Vendors model

    Arguments:
        AuditableModel {object} -- Auditable class
    """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logo/%Y/%M/%d')
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        """Meta"""
        db_table = 'vendors'
