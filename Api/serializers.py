from django.contrib.auth import get_user_model
from rest_framework import serializers

from Blog.models import BlogPost

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            # 'username',
            'title',
            'author',
            'description',
            'created_at',
            'updated_at',
        )
        model = BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 
            'get_full_name',
            'username',
            'email',
            'date_joined',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
        )