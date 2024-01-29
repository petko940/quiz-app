import os

from rest_framework.permissions import BasePermission


class JsTokenPermission(BasePermission):
    def has_permission(self, request, view):
        js_token = request.headers.get('X-JSToken')
        return js_token == os.getenv('JS_TOKEN')
