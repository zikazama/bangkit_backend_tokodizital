from django.urls import path
from .views import HomeAPI

urlpatterns = [
    path('', HomeAPI.as_view(), name='home'),
]