from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password'
        ]

        labels ={
            'username': 'Nombre de Usuario',
            'email':'Correo electrónico',
            'password': 'Contraseña'
        }

        widgets ={
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Tu nombre'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'palceholder':'correo@email.com'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = 'usuario@email.com'


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

        return user