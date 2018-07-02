import requests
from django import http
from django.conf import settings
from django.template import engines
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_auth.views import LogoutView
from mongoengine import *
from django_mongoengine import Document, EmbeddedDocument, fields


connect("microj")

@csrf_exempt
def catchall_dev(request, upstream="http://localhost:3000"):
    # Proxy HTTP requests to frontend dev server in development.
    upstream_url = upstream + request.path
    method = request.META['REQUEST_METHOD'].lower()
    response = getattr(requests, method)(upstream_url, stream=True)
    content_type = response.headers.get("Content-Type")

    if request.META.get('HTTP_UPGRADE', '').lower() == 'websocket':
        return http.HttpResponseRedirect(upstream_url + request.path)

    elif content_type == "text/html; charset=UTF-8":
        return http.HttpResponse(content=engines["django"].from_string(response.text).render(),
                                 status=response.status_code,
                                 reason=response.reason)

    else:
        return http.StreamingHttpResponse(streaming_content=response.iter_content(2 ** 12),
                                          content_type=content_type,
                                          status=response.status_code,
                                          reason=response.reason)


catchall_prod = TemplateView.as_view(template_name="index.html")

catchall = catchall_dev if settings.DEBUG else catchall_prod


class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)