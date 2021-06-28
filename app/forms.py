from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class MyUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)


class MyLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, label='メールアドレス')
    password = forms.CharField(widget=forms.PasswordInput, label="パスワード")
