from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Powtórz hasło'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    username = forms.CharField(max_length=40, help_text='')
    email = forms.EmailField(max_length=40)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text='Minimum 8 znaków', min_length=8, max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text='')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
    