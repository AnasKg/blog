from rest_framework import viewsets, filters

from post.models import Tag, Category, Post
from post.api.serializers import TagSerializer, CategorySerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at', 'views', 'category__title']
    ordering = ['-created_at']
    filterset_fields = ['author', 'category', 'tags', 'created_at']
