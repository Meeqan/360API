from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.base_model import BaseModel


class User(AbstractUser, BaseModel):
    """Custom user model"""

    BUSINESS = 'BUS'
    REGULAR = 'REG'
    ACCOUNT_TYPE_CHOICES = (
        (BUSINESS, 'Business'),
        (REGULAR, 'Regular User'),
    )

    account_type = models.CharField(
        max_length=3,
        choices=ACCOUNT_TYPE_CHOICES,
        default=REGULAR,
    )

    def __str__(self):
        return self.email

    class Meta:
        """Meta"""
        db_table = 'users'
