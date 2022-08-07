from django.urls import path

from .views import CustomUserListAPIView
urlpatterns = [
    path('api/v1/user/', CustomUserListAPIView.as_view()),
]