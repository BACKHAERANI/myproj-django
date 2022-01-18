from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from news.forms import ArticleForm
from news.models import Article
from news.serializers import ArticleSerializer
import json
from django.http import HttpResponse
from rest_framework.generics import ListAPIView

article_list = ListView.as_view(model=Article)

article_new = CreateView.as_view(
    model=Article, form_class=ArticleForm, success_url=reverse_lazy("news:article_list")
)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않음
        # 대신 키워드 인자를 통한 속성 지정을 지원함
        serializer.save(author=self.request.user)
