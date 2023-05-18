from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=15)