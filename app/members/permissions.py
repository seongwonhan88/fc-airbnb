from rest_framework import authentication, permissions


class BearerAuthentication(authentication.TokenAuthentication):
    """
    postman 에서 token header 값에 'Token'대신에 'Bearer'가 오기 때문에
    TokenAuth를 상속받으면서 keyword 값만 Bearer로 변경
    """
    keyword = 'Bearer'


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsReviewer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.guest == request.user