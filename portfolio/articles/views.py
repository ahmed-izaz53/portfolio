from django.shortcuts import render
from django.views.generic import *
from .models import Article

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context = {
            "articles": Article.objects.all()
        }
        return context

class About(TemplateView):
    template_name="about.html"

class Contact(TemplateView):
    template_name="contact.html"

class ArticleDetail(TemplateView):
    template_name = "article_detail.html"
    def get_context_data(self, slug, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context = {
            "article" : Article.objects.get(slug=slug)
        }
        return context