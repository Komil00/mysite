from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreatorForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('age','address','job')

class CustomUserChangeForm(UserChangeForm):
    class Mete(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields        

