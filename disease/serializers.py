# create disease serializer
from rest_framework import serializers
from disease.models import Disease
from history.models import History
from product.serializers import ProductSerializer
from authentication.serializers.profile_serializer import ProfileSerializer

class DiseaseSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, )

    class Meta:
        model = Disease
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class DetectDiseaseSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)

    class Meta:
        model = History
        fields = '__all__'