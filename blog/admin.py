from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    pass

