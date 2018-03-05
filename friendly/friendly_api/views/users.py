from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters
from ..models.users import User
from ..serializers.users import UserSerializer
from .. import permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework_extensions.mixins import NestedViewSetMixin


class UsersView(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Users Api View
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsResourceOwner,)
    authentication_classes = (TokenAuthentication,)
    filter_backend = filters.SearchFilter
    search_fields = ("name", "email")
