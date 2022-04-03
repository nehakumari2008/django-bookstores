from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from books_store.models import Store, Book


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields= ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=['name', 'author', 'price', 'no_of_copies']



class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=100)
    password = forms.CharField(label="Password", max_length=100)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email