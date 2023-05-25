from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator

from applibs.response import prepare_error_response
from .models import Blog
from .serializers import BlogListSerializer, BlogSerializer

class BlogListAPI(APIView) :

    def get(self, request) :
        query_params = request.query_params

        limit = int(query_params.get('limit', 10))
        page = int(query_params.get('page', 1))

        blogs = Blog.objects.all().order_by('-timestamp')
        blogs_paginator = Paginator(blogs, limit)
        blog_page = blogs_paginator.get_page(page)

        data = {
            "result" : blog_page,
            "meta" : {
                "total_pages" : blogs_paginator.num_pages,
                "current_page" : page,
                "limit" : limit,
                "total_item" : blogs_paginator.count,
                "has_next" : blog_page.has_next(),
                "has_previous" : blog_page.has_previous(),
            }
        }

        serializer = BlogListSerializer(data)
        return Response(serializer.data)
    
class BlogAPI(APIView) :
    
    def get(self, request, id) :

        blog = Blog.objects.filter(pk=id).first()
        if(blog == None) :
            return Response(prepare_error_response("Blog not exists!"),
                        status.HTTP_400_BAD_REQUEST)

        serializer = BlogSerializer(blog)
        return Response(serializer.data)






