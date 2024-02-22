from datetime import datetime, timedelta

import jwt
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is not None:
            jwt_token = self.generate_jwt_token(user)
            response_data = {
                'id': user.id,
                'username': user.username,
                'jwt_token': jwt_token,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'non_field_errors': ['Unable to log in with provided credentials.']},
                            status=status.HTTP_400_BAD_REQUEST)

    def generate_jwt_token(self, user):
        expiration_time = datetime.utcnow() + timedelta(days=1)
        token_payload = {
            'id': user.id,
            'username': user.username,
            'exp': expiration_time,
        }

        token = jwt.encode(token_payload, 'JWT', algorithm='HS256')
        return token


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
