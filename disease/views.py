import os
import gcsfs
import h5py
from PIL import Image

from django.shortcuts import render
from django.utils.decorators import method_decorator
from tensorflow.keras.models import load_model

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.apps import apps


from disease.services.predict_type import predict_type
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
from datetime import datetime

@method_decorator(csrf_exempt, name='dispatch')
class DetectDiseaseAPI(APIView):
    serializer_class = DetectDiseaseSerializer
    permission_classes = [IsAuthenticated]

    # def __init__(self):
    #     super(DetectDiseaseAPI, self).__init__()
    #     DiseaseConfig = apps.get_app_config('disease')
    #     self.model_type = DiseaseConfig.model_type
    #     self.model_potato = DiseaseConfig.potato_model
    #     self.model_apple = DiseaseConfig.apple_model
        
    def post(self, request):

        data = request.data.copy()

        if request.user and request.user.is_authenticated:
            data['user'] = request.user.id

        serializer = self.serializer_class(data=data)
        valid = serializer.is_valid(raise_exception=True)

        # TODO: get disease from ML
        # predicted_disease = predict_type(Image.open(data['image']), self.model_type, self.model_potato, self.model_apple)
        # disease = Disease.objects.filter(name = predicted_disease).first()
        # # END TODO
        
        # serializer.validated_data['disease'] = disease

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
            'data': "NOT YET IMPLEMENT!!",
        }

        return Response(response, status=status_code)
    
    #JUST FOR TESTING!
    def get(self, request) :
        ROOT_PATH = os.path.abspath(os.curdir)
        print(ROOT_PATH)
        try : 
            ITEM_LIST = os.listdir(ROOT_PATH)
            return Response({"file" : ITEM_LIST,
                             "path" : ROOT_PATH})

        except Exception as ex:
            return Response({"file" : ROOT_PATH})
