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
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]  DRF디폴트설정
    # 보여 주는 데이터의 범위를 결정하는 것은 serializer이다.
    #
    # def get_serializer_class(self):
    #     return ArticleSerializer
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     query = self.request.guery_params.get("query", "")
    #     if query:
    #         qs = qs.filter(title_icontains=query)
    #     year = self.request.guery_params.get("year", "")
    #     if year:
    #         qs = qs.filter(created_at__year=year)
    #     return qs


# article_list = ListAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializer,
# )
# def article_list(request):
#     qs = Article.objects.all()
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#     # [{"id": article.id,
#     #          "title": article.title,
#     #          "content": article.content,
#     #          "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,}
#     #         for article in qs]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)
