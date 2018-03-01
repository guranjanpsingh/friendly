from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.users import User
from ..serializers.users import UserSerializer

class UsersView(APIView):
    """
    Users Api View
    """

    def get(self, request, format = None):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)