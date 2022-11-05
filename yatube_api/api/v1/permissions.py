from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверяет является ли пользователь автором для изменения записи.
    Или является ли тип запроса безопасным.
    """

    def has_object_permission(self, request, view, obj):
        return (obj.author_id == request.user.id
                or request.method in permissions.SAFE_METHODS)
