
from rest_framework import serializers

from .models import User
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long.")
        return value

    def validate_email(self, value):
        if not "@" in value:
            raise serializers.ValidationError("Invalid email format.")
        return value

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email','password']

class LiveFeedSerializer(serializers.Serializer):
    message = serializers.CharField()

class BinanceLiveFeedSerializer(serializers.Serializer):
    data = serializers.JSONField()
