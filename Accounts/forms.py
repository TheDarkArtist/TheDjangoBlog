from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'name',
            # 'username',
            'email'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'name',
            'username',
            'email',
        )
