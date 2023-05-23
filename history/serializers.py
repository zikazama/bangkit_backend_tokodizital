from rest_framework import serializers
from history.models import History
from disease.serializers import DiseaseSerializer

class HistorySerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)

    class Meta:
        model = History
        fields = '__all__'
        read_only_fields = ('timestamp', 'id')