from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']


class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_photo']


class FollowUserButton(forms.Form):
    user_to_follow = forms.CharField(widget=forms.HiddenInput())


class SearchUser(forms.Form):
    search = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Rechercher un utilisateur'
            }
        )
    )
    search_user_id = forms.BooleanField(widget=forms.HiddenInput, initial=True)
