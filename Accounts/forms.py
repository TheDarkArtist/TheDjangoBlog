from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'username',
            'email'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'username',
            'email',
        )
