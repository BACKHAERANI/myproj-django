from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cookierun.views import CharacterViewSet

app_name = "cookierun"


router = DefaultRouter()


router.register("characters", CharacterViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
