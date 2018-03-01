from rest_framework.serializers import ModelSerializer
from ..models import users

class UserSerializer(ModelSerializer):
    class Meta:
        model = users.User
        fields = ("name", "email", "password")