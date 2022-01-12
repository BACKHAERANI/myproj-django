from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets
from news.forms import ArticleForm
from news.models import Article
from news.serializers import ArticleSerializer

article_list = ListView.as_view(model=Article)

article_new = CreateView.as_view(model=Article, form_class=ArticleForm, success_url=reverse_lazy("news:article_list"))


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
