from django.http import HttpResponse
from rest_framework import viewsets
from blog.models import Post
from blog.serializers import PostSerializer
import json


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



def post_list(request):
    qs = Post.objects.all()
    data = [{"id": Post.id, "title": Post.title, "content": Post.content} for Post in qs]
    json_string = json.dumps(data)
    return HttpResponse(json_string)