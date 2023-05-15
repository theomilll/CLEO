from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cart
from .models import CreditCard
from django.core.exceptions import ValidationError

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
    
class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['name', 'card_number', 'expiry_date', 'cvv_code']

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if len(str(card_number)) != 16:
            raise ValidationError('Credit card number must be 16 digits long.')
        return card_number

    def clean_cvv_code(self):
        cvv_code = self.cleaned_data.get('cvv_code')
        if len(str(cvv_code)) != 3:
            raise ValidationError('CVV code must be 3 digits long.')
        return cvv_code