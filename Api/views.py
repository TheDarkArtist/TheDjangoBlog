from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from Blog.models import BlogPost
from .serializers import BlogSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class APIHome(TemplateView):
    template_name = "api_home.html"

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
