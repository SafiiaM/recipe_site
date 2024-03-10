from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    """
    Пользователь системы
    """

    def __str__(self):
        return self.username

class Category(models.Model):
    """
    Категория рецепта.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

class Recipe(models.Model):
    """
    Рецепт.
    """
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, default=None)
    ingredients = models.TextField(null=True, default=None)
    steps = models.TextField()
    time_cook = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    photo = models.ImageField(upload_to='img/', null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    categories = models.ManyToManyField(Category, related_name='recipes')

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]



