from django.urls import path
from .views import CommentAPI

urlpatterns = [
    path('submit/', CommentAPI.as_view(), name='blog_list'),
    path('<int:id>/', CommentAPI.as_view(), name='blog_detail')
]