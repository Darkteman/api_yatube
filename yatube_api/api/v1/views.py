from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Comment, Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """
    Объединяет логику для набора связанных представлений модели Post.
    При GET-запросе списка объектов, указав параметры limit и offset,
    выдача должна работать с пагинацией.
    """
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создает Пост с заданым полем author."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Объединяет логику для набора связанных представлений модели Group.
    Представления работают только с безопасными запросами.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Объединяет логику для набора связанных представлений модели Comment.
    """
    permission_classes = [IsAuthorOrReadOnly, ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Формирует queryset из комменатрием n-ого поста."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post=post.id)

    def perform_create(self, serializer):
        """Создает Комментарий с задаными полями: author, post."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    Объединяет логику для набора связанных представлений модели Follow.
    Все допустимые запросы разрешены только аутент. пользователям.
    Доступен поиск по подпискам по параметру search.
    """
    permission_classes = [IsAuthenticated, ]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Формирует queryset из подписок автора."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Создает связь с заданым полем following."""
        if serializer.validated_data['following'] == self.request.user:
            raise ValidationError('Нельзя подписаться на самого себя!')
        serializer.save(user=self.request.user)
