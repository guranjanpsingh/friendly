from rest_framework import serializers
from ..models.userlocations import UserLocation


class UserLocationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLocation
        fields = ('id', 'user', 'longitude', 'latitude', 'last_updated')