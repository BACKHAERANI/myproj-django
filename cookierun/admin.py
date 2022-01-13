from django.contrib import admin
from cookierun.models import Character


@admin.register(Character)
class Character(admin.ModelAdmin):
    pass
