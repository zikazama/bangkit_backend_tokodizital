from django.urls import path
from .views import BlogAPI, BlogListAPI

urlpatterns = [
    path('', BlogListAPI.as_view(), name='blog_list'),
    path('<int:id>/', BlogAPI.as_view(), name='blog_detail')
]