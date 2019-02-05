from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class BaseViewSet(viewsets.ViewSet):
    """Base ViewSet"""

    __abstract__ = True

    model_class = None
    serializer_class = None

    def list(self, request):
        """

        Args:
            request:

        Returns:

        """

        queryset = self.model_class.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """

        Args:
            request:
            pk:

        Returns:

        """
        queryset = self.model_class.objects.all()
        vendor = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(vendor)
        return Response(serializer.data)

    def create(self, request):
        """

        Args:
            request:

        Returns:

        """
        return Response(f'create{self.model_class._meta.db_table}')

    def update(self, request, pk=None):
        """

        Args:
            request:
            pk:

        Returns:

        """
        return Response('Update')

    def partial_update(self, request, pk=None):
        """

        Args:
            request:
            pk:

        Returns:

        """
        return Response('Partial update')

    def destroy(self, request, pk=None):
        """

        Args:
            request:
            pk:

        Returns:

        """
        return Response('Delete')

    def handle_exception(self, exc):
        """

        Args:
            exc:

        Returns:

        """

        if isinstance(exc, Http404):
            return Response(
                {
                    'status': 'error',
                    'message': f'No {self.model_class._meta.db_table} found.'
                },
                status=status.HTTP_404_NOT_FOUND)

        return super().handle_exception(exc)
