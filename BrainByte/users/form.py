from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']