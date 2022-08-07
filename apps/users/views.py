from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserListAPIView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get a list of users",
        responses={'200': CustomUserSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)