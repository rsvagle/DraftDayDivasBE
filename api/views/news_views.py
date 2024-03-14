from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods


# All News Articles
class NewsArticleListView(generics.ListAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

# Specific News Article
class NewsArticleView(APIView):
    def get(self, request, id, format=None):
        try:
            article = NewsArticle.objects.get(id=id)
            serializer = NewsArticleSerializer(article)
            return Response(serializer.data)
        except NewsArticle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# All Injury Reports
class InjuryReportArticleView(generics.ListAPIView):
    queryset = InjuryReportArticle.objects.all()
    serializer_class = InjuryReportArticleSerializer
