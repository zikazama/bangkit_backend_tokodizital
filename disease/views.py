import os
from PIL import Image

from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.apps import apps


from disease.services.predict_type import predict_type
from .models import Disease
from .serializers import DetectDiseaseSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@method_decorator(csrf_exempt, name='dispatch')
class DetectDiseaseAPI(APIView):
    serializer_class = DetectDiseaseSerializer
    # permission_classes = [IsAuthenticated]

    def __init__(self):
        super(DetectDiseaseAPI, self).__init__()
        DiseaseConfig = apps.get_app_config('disease')
        self.model_type = DiseaseConfig.model_type
        self.model_potato = DiseaseConfig.potato_model
        self.model_apple = DiseaseConfig.apple_model
        self.model_corn = DiseaseConfig.corn_model
        
    def post(self, request):

        data = request.data.copy()
        
        if request.user and request.user.is_authenticated:
            data['user'] = request.user.id

        serializer = self.serializer_class(data=data)

        valid = serializer.is_valid(raise_exception=True)
        
        predicted_disease = predict_type(Image.open(data['image']), self.model_type, 
                                         self.model_potato, self.model_apple, self.model_corn)
        disease = Disease.objects.filter(name = predicted_disease).first()
        
        serializer.validated_data['disease'] = disease

        if valid and request.user and request.user.is_authenticated:
            serializer.save()
            print("saved")
        else:
            serializer.validated_data['timestamp'] = datetime.now()
            print("not saved")
            
        status_code = status.HTTP_201_CREATED

        response = {
            'success': True,
            'statusCode': status_code,
            'data': serializer.data,
        }

        return Response(response, status=status_code)