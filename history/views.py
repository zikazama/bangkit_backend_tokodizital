from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import History
from .serializers import HistoryListSerializer
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

@method_decorator(csrf_exempt, name='dispatch')
class HistoryAPI(APIView):
    def get(self, request):
        query_params = request.query_params

        limit = int(query_params.get('limit', 10))
        page = int(query_params.get('page', 1))

        histories = History.objects.filter(user=request.user).order_by('-timestamp')
        histories_paginator = Paginator(histories, limit)
        history_page = histories_paginator.get_page(page)

        data = {
            "result" : history_page,
            "meta" : {
                "total_pages" : histories_paginator.num_pages,
                "current_page" : page,
                "limit" : limit,
                "total_item" : histories_paginator.count,
                "has_next" : history_page.has_next(),
                "has_previous" : history_page.has_previous(),
            }   
        }

        serializer = HistoryListSerializer(data)

        return Response(serializer.data)
