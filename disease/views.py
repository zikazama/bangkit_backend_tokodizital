from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Disease
from .serializers import DiseaseSerializer, DetectDiseaseSerializer
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from disease.services.predict_type import predict_type


@method_decorator(csrf_exempt, name='dispatch')
class DetectDiseaseAPI(APIView):
    serializer_class = DetectDiseaseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()
        data['user'] = request.user.id
        serializer = self.serializer_class(data=data)
        valid = serializer.is_valid(raise_exception=True)

        # TODO: get disease from ML
        predicted_disease = predict_type(Image.open(data['image']))
        disease = Disease.objects.filter(name = predicted_disease).first()
        # END TODO
        
        serializer.validated_data['disease'] = disease

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'data': serializer.data,
            }

            return Response(response, status=status_code)