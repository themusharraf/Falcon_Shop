from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.models import User
from apps import models


class UsersCreationForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super(UsersCreationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.pop('password2')
        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')


class ProductForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'image', 'price', 'description', 'long_description', 'discount', 'number', 'shop_cost', 'tags'
                  , 'specification')
        model = models.Product
