from rest_framework import serializers
from blog.models import Blog
from authentication.serializers import user_serializer

class PaginationSerializer(serializers.Serializer) :
    total_pages = serializers.CharField()
    current_page = serializers.CharField()
    limit = serializers.CharField()
    total_item = serializers.CharField()
    has_next = serializers.BooleanField()
    has_previous = serializers.BooleanField()

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class BlogListSerializer(serializers.Serializer) :
    result = BlogSerializer(many=True)
    meta = PaginationSerializer()