from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import ArticleViewSet, article_list, article_new

app_name ='news'


router = DefaultRouter()
router.register("article", ArticleViewSet)

urlpatterns = [path('article/', article_list, name="article_list"),
               path('article/new/', article_new, name="article_new"),
               path('api/', include(router.urls))]