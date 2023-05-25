from rest_framework import serializers
from history.models import History
from disease.serializers import DiseaseSerializer

class PaginationSerializer(serializers.Serializer) :
    total_pages = serializers.CharField()
    current_page = serializers.CharField()
    limit = serializers.CharField()
    total_item = serializers.CharField()
    has_next = serializers.BooleanField()
    has_previous = serializers.BooleanField()

class HistorySerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)

    class Meta:
        model = History
        fields = '__all__'
        read_only_fields = ('timestamp', 'id')
    
class HistoryListSerializer(serializers.Serializer) :
    result = HistorySerializer(many=True)
    meta = PaginationSerializer()