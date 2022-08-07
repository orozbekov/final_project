from django.urls import path

from .views import CategoryListAPIView, FoodListAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('food/', FoodListAPIView.as_view()),
]