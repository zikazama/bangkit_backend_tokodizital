from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import History
from .serializers import HistorySerializer
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class HistoryAPI(APIView):
    def get(self, request):
        query_params = request.query_params
        limit = int(query_params.get('limit', 10))
        offset = int(query_params.get('offset', 0))

        histories = History.objects.filter(user=request.user).order_by('-timestamp')[offset:offset+limit]
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
