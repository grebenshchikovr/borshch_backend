from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import forms

from .models import BorshchUser

class BorshchUserLoginForm(AuthenticationForm):
    class Meta:
        model = BorshchUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(BorshchUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class BorshchUserRegisterForm(UserCreationForm):
    class Meta:
        model = BorshchUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

        return data
