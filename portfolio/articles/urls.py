from django.urls import path
from . import views
app_name = "articles"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.About.as_view(), name="about"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("article-detail/<slug:slug>/", views.ArticleDetail.as_view(), name="article_detail"),
]