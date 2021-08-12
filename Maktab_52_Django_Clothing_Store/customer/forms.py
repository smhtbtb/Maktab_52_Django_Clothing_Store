from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from customer.models import *


class LoginUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField()
    phone = forms.CharField(required=True, max_length=11, help_text=_('Required field. For example 09123456789'))

    class Meta:
        model = User
        fields = (
            'phone',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_deta['first_name']
    #     user.last_name = self.cleaned_deta['last_name']
    #     user.phone = self.cleaned_deta['phone']
    #     user.email = self.cleaned_deta['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user


# class UpdateAddressForm(forms.ModelForm):
#     model = Address
#     fields = '__all__'

class AddressFrom(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'province', 'detail', 'post_code']
