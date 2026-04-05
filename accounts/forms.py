from django import forms
from django.forms import ModelForm, ValidationError
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Parolni kiriting'})
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlash",
        widget=forms.PasswordInput(attrs={'placeholder': 'Parolni qayta kiriting'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'age', 'username', 'password', 'image']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and username.lower().startswith('a'):    
            raise ValidationError("Username 'a' harfi bilan boshlanishi mumkin emas!")
        if username and len(username) < 8:
            raise ValidationError("Username kamida 8 ta belgidan iborat bo‘lishi kerak!")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        print(password, password2)

        if password and password2 and password != password2:
            raise ValidationError("Parollar mos emas!")

        # boshqa umumiy validatsiyalar qo‘shish mumkin

        return cleaned_data