from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.accounts.models import User, Profile, OTP
from drf_spectacular.utils import extend_schema_field


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'date_joined']
        read_only_fields = ['id', 'date_joined']
    
    def get_profile(self, obj):
        return ProfileSerializer(obj.profile).data if obj.profile else {}
    
    

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    username = serializers.CharField(max_length=150)
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.get_or_create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user or not user.is_active:
            raise serializers.ValidationError('Invalid credentials')
        return {'user': user}


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['user_id', 'bio', 'avatar', 'followers_count', 'following_count', 'is_private']
