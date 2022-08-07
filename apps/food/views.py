from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from drf_yasg.utils import swagger_auto_schema

from .models import Category, Food
from .serializers import CategorySerializer, FoodSerializer


class CategoryListAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Список всех категории.',
        responses={
            '200': CategorySerializer(many=True),
        },
    )

    def get(self, request):
        """
        Список всех категории.
        """
        category = Category.objects.all()
        srz = CategorySerializer(category, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Создание категории.',
        request_body=CategorySerializer(many=False),
        responses={
            '201': CategorySerializer(many=False),
        },
    )
    
    def post(self, request):
        """
        Созание категории с заданными данными.
        """
        request_body = request.data
        new_category = Category.objects.create(
            title=request_body['title']
        )
        srz = CategorySerializer(new_category, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    
class FoodListAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Список всех блюд.',
        responses={
            '200': CategorySerializer(many=True),
        },
    )

    def get(self, request):
        food = Food.objects.select_related('category').all()
        srz = FoodSerializer(food, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Создание еды.',
        request_body=CategorySerializer(many=False),
        responses={
            '201': CategorySerializer(many=False),
        },
    )

    def post(self, request):
        request_body = request.data
        new_food = Food.objects.create(
            id=request_body['id'], category=request_body['category_id'], name=request_body['name'], 
            description=request_body['description'], recipe=request_body['recipe'], 
            youtube_url=request_body['youtube_url']
        )
        srz = FoodSerializer(new_food, many=True)
        return Response(srz.data, status=status.HTTP_201_CREATED)