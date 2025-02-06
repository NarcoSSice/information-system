from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class AddPublicationForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('pk'), widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Default select example'}))
    monograph_check = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    collective_monograph = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    professional_publication = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    foreign_editions = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    mnbd_publications = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    foreign_authors = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    publications_with_students = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    published = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    ready_for_print = forms.BooleanField(widget=forms.CheckboxInput, required=False)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Логін'}
                               ))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'type': 'password',
                                           'placeholder': 'Введіть пароль'}
                                ))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'type': 'password',
                                           'placeholder': 'Підтвердіть пароль'}
                                ))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Електронна пошта'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Ім\'я'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Прізвище'}),
        }

    def clean(self):
        clean_data = super(RegisterUserForm, self).clean()
        email = clean_data.get('email')
        first_name = clean_data.get('first_name')
        last_name = clean_data.get('last_name')
        if not all([email, first_name, last_name]):
            raise forms.ValidationError('У формі є незаповнені поля')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Логін'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Введіть пароль'}))