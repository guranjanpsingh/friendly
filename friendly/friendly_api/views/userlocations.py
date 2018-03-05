from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ..serializers import userlocations
from ..models.userlocations import UserLocation
from rest_framework_extensions.mixins import NestedViewSetMixin


class UserLocationsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    user locations view set
    """
    serializer_class = userlocations.UserLocationsSerializer
    queryset = UserLocation.objects.all()