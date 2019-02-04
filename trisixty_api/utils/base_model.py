"""Base model """

from django.db import models
from .pushID import PushID


class BaseModel(models.Model):
    """Base model"""

    id = models.CharField(max_length=30, primary_key=True, unique=True,
                          default=PushID().next_id())
    deleted = models.BooleanField(default=False, null=True)

    def save(self, *args, **kwargs):
        """Overwrites the save method

        Args:
            *args:
            **kwargs:

        Returns:

        """

        super().save(*args, **kwargs)

    class Meta:
        """
        Meta
        """
        abstract = True
