from django import forms
from .models import Profile
from utils.validators import phone_number_validator
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True, label='Телефон',
                            validators=[phone_number_validator],
                            help_text='Номер телефона в формате "+7" или "8"')

    class Meta:
        model = Profile
        fields = ('username', 'phone', 'email', 'password1', 'password2',)

