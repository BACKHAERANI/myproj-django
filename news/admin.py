from django.contrib import admin
from news.models import Article


@admin.register(Article)
class Article(admin.ModelAdmin):
    pass
