from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Blog
from blog.serializers import BlogSerializer
from history.models import History
from history.serializers import HistorySerializer
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class HomeAPI(APIView):
    def get(self, request):

        data = {
            'is_authenticated': request.user.is_authenticated,
            'history' : [],
        }

        if request.user and request.user.is_authenticated:
            histories = History.objects.filter(user=request.user).order_by('-timestamp')[0:5]
            historyListSerializer = HistorySerializer(histories, many=True)
            data['history'] = historyListSerializer.data

        blogs = Blog.objects.all().order_by('-timestamp')[0:5]
        blogListSerializer = BlogSerializer(blogs, many=True)
        data['blogs'] = blogListSerializer.data
    
        return Response(data, status=status.HTTP_200_OK)