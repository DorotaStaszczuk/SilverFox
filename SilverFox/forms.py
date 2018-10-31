from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from SilverFox.models import User, Photo


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['date_added']
        widgets = {
            'camera_type': forms.Select,
            'camera_name': forms.Select,
            'film_type': forms.Select,
            'film_name': forms.Select,
            'film_iso': forms.Select,
            'film_options': forms.CheckboxInput,
            'photo_options': forms.CheckboxInput,
        }


class AddUserInfoForm(ModelForm):
    class Meta:
        model = User
        exclude = ['login']


class EditPhotoForm(forms.Form):
    pass


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, label="Hasło")


class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField()


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
