from django.http import HttpResponse
from rest_framework import viewsets
from cookierun.models import Character
from cookierun.serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
