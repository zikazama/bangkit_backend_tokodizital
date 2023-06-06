from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=False)
    phone_number = serializers.CharField(max_length=15, required=False)
    email = serializers.CharField(required=False, max_length=100)
    image = serializers.ImageField(required=False)