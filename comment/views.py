from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator

from applibs.response import prepare_error_response, prepare_success_response
from .serializers import CommentListSerializer, SubmitCommentSerializer, CommentSerializer
from .models import Comment

class CommentAPI(APIView) :
    
    def __init__(self) :
        super(CommentAPI, self).__init__()
        self.comment_serializer = CommentSerializer
        self.comment_list_serializer = CommentListSerializer
        self.submit_comment = SubmitCommentSerializer

    def get(self, request, id) :
        query_params = request.query_params

        limit = int(query_params.get('limit', 10))
        page = int(query_params.get('page', 1))

        comment = Comment.objects.filter(blog_id = id)
        comments_paginator = Paginator(comment, limit)
        comment_page = comments_paginator.get_page(page)

        data = {
            "result" : comment_page,
            "meta" : {
                "total_pages" : comments_paginator.num_pages,
                "current_page" : page,
                "limit" : limit,
                "total_item" : comments_paginator.count,
                "has_next" : comment_page.has_next(),
                "has_previous" : comment_page.has_previous(),
            }
        }

        serializer = self.comment_list_serializer(data)
        return Response(serializer.data)
    
    def post(self, request) :
        submit_comment_serializer = self.submit_comment(data=request.data)

        if not submit_comment_serializer.is_valid():
            return Response(prepare_error_response(submit_comment_serializer.errors),
                            status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        message = submit_comment_serializer.validated_data['message']
        blog = submit_comment_serializer.validated_data['blog']

        comment = Comment.objects.create(message = message,
                                            user = user,
                                            blog_id = blog)
        

        return Response(prepare_success_response(data=self.comment_serializer(comment).data),
                            status=status.HTTP_201_CREATED)
        




