from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

# API views with generics views and mixins

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer