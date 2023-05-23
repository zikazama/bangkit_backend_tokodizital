from django.urls import path
from .views import DetectDiseaseAPI
urlpatterns = [
    path('', DetectDiseaseAPI.as_view(), name='detect_disease'),
]