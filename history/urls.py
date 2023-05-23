from django.urls import path
from .views import HistoryAPI

urlpatterns = [
    path('', HistoryAPI.as_view(), name='history'),
]