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


class NewsArticleListView(generics.ListAPIView):
    serializer_class = NewsArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned news articles to a given limit,
        by filtering against a `limit` query parameter in the URL.
        """
        limit = self.request.query_params.get('limit', None)
        if limit is not None:
            try:
                limit = int(limit)
                queryset = NewsArticle.objects.order_by('-created_at')[:limit]
            except ValueError:
                # Handle the case where limit is not an integer
                pass
        else:
            queryset = NewsArticle.objects.order_by('-created_at').all()
        return queryset

# Specific News Article
class NewsArticleView(APIView):
    def get(self, request, id, format=None):
        try:
            article = NewsArticle.objects.get(id=id)
            serializer = NewsArticleSerializer(article)
            return Response(serializer.data)
        except NewsArticle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# Player News Articles
class PlayerNewsArticlesView(generics.ListAPIView):
    def get(self, request, id, format=None):

        player = FootballPlayer.objects.get(id=id)
        name = player.first_name + " " + player.last_name

        try:
            article = NewsArticle.objects.filter(article_content__contains=name).all()
            serializer = NewsArticleSerializer(article, many=True)
            return Response(serializer.data)
        except NewsArticle.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

# All Injury Reports
class AllInjuryReportArticlesView(generics.ListAPIView):
    queryset = InjuryReportArticle.objects.all()
    serializer_class = InjuryReportArticleSerializer

# All Injury Reports
class AllInjuryReportsForPlayerView(generics.ListAPIView):
    def get(self, request, id, format=None):
        try:
            articles = InjuryReportArticle.objects.filter(player_id=id).all()
            serializer = InjuryReportArticleSerializer(articles, many=True)
            return Response(serializer.data)
        except InjuryReportArticle.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

# Individual Injury Report
class InjuryReportArticleView(APIView):
    def get(self, request, id, format=None):
        try:
            article = InjuryReportArticle.objects.get(id=id)
            serializer = InjuryReportArticleSerializer(article)
            return Response(serializer.data)
        except InjuryReportArticle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)