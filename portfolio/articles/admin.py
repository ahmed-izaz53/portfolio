from django.contrib import admin
from .models import Article, ArticleCategory
# Register your models here.
admin.site.register(ArticleCategory)
admin.site.register(Article)