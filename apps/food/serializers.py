from rest_framework import serializers

from .models import Category, Food

class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для категории.
    """
    
    class Meta:
        model = Category
        fields = ('id', 'title',)
        
class FoodSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модельки еды.
    """
   
    class Meta:
        model = Food
        fields = ('id', 'category_name', 'name', 'image_url', 'description', 'recipe', 'youtube_url',)

    