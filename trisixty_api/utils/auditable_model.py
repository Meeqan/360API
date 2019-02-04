""" Module for auditable model"""

from datetime import datetime
from django.db import models
from .base_model import BaseModel


class AuditableModel(BaseModel):
    """
    Auditable base model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, blank=True)
    updated_by = models.CharField(max_length=200, blank=True)
    deleted_by = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        """Overwrites the save method

        Args:
            *args:
            **kwargs:

        Returns:

        """

        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        """
        Meta
        """
        abstract = True
