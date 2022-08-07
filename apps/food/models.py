from django.db import models

class Category(models.Model):
    """
    Модель для категории.
    """
    title = models.CharField("Категория", max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Food(models.Model):
    """
    Модель для еды.
    """
    category = models.ForeignKey(Category, verbose_name="Категория", related_name="foods", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=250)
    image = models.ImageField("Изображение", upload_to='images/')
    description = models.TextField("Описание", blank=True)
    recipe = models.TextField("Рецепт")
    slug = models.SlugField(max_length=200, unique=True)
    youtube_url = models.URLField("Сыылка на YouTube", max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    @property
    def category_name(self):
        return self.category.title
    
    @property
    def image_url(self):
        return 'http://127.0.0.1:8000' + self.image.url

    def __str__(self):
        return self.name


