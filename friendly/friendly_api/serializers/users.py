from rest_framework import serializers
from ..models import users, userlocations


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users.User
        locations = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        fields = ("id", "name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}