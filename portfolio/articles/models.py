from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleCategory(models.Model):
    category_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

#foreignkey means many to one relation.. there will be so many article under one user..
class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, default=None)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def summary(self):
        return self.description[:30]+"...."

