from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.mixins import LoginRequiredMixin

from Blog.models import BlogPost
from .serializers import BlogSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class APIHome(LoginRequiredMixin, TemplateView):
    login_url='login'
    template_name = "api_home.html"

class BlogViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url='login'
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class UsersViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url='login'
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
