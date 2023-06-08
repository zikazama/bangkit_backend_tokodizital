from rest_framework import serializers
from comment.models import Comment
from authentication.serializers.profile_serializer import ProfileSerializer
from blog.models import Blog

class PaginationSerializer(serializers.Serializer) :
    total_pages = serializers.CharField()
    current_page = serializers.CharField()
    limit = serializers.CharField()
    total_item = serializers.CharField()
    has_next = serializers.BooleanField()
    has_previous = serializers.BooleanField()

class CommentSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.Serializer) :
    result = CommentSerializer(many=True)
    meta = PaginationSerializer()

class SubmitCommentSerializer(serializers.Serializer) :
    message = serializers.CharField(min_length = 1)
    id_blog = serializers.IntegerField()

    def validate(self, attrs):
        id_blog = attrs.get("id_blog", None)
        message = attrs.get("message", None)

        blog = Blog.objects.filter(pk = id_blog).first()
        if not blog :
            raise serializers.ValidationError(
                {"id_blog": "id_blog not exists."})
        
        response_data = {
            'message': message,
            'blog': blog,

        }
        return response_data
