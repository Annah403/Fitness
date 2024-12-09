from django import forms
from django.contrib.auth.models import User

from fitness.models import Exercise, Contact


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title'}),
            'desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Description'}),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'images/*',
                'title': 'Upload your image here'})
        }

class UserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),

        }
    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password_confirm']

class ContactForm(forms.ModelForm):
        class Meta:
            model = Contact
            fields = ['name', 'email', 'phone', 'desc']
