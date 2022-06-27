from rest_framework import generics
from rest_framework.authentication import SessionAuthentication

from blog.api.serializers import PostSerializer
from blog.models import Post
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

# API views with generics views and mixins

class PostList(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer