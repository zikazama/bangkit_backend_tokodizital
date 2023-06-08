from django.urls import path
from .views import CommentAPI, SubmitCommentAPI

urlpatterns = [
    path('submit/', SubmitCommentAPI.as_view(), name='submit_comment'),
    path('<int:id>/', CommentAPI.as_view(), name='comment_list')
]