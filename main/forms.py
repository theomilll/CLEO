from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cart

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'name' : 'username_r'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'name' : 'email_r'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name' : 'password1_r'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'name' : 'password2_r'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''

class CartForm(forms.Form):
    text_box_obs = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Alguma observação?'}), required=False)