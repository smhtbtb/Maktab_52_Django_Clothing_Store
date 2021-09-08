from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, PasswordChangeForm, \
    AuthenticationForm
from django.utils.translation import gettext_lazy as _

from customer.models import *


# First Login Form
class LoginUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# Second Login Form
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'password'}
    ))


# class RegistrationForm(UserCreationForm):
#     # email = forms.EmailField()
#     phone = forms.CharField(required=True, max_length=11, help_text=_('Required field. For example 09123456789'))
#
#     class Meta:
#         model = User
#         fields = (
#             'phone',
#             'email',
#             'first_name',
#             'last_name',
#             'password1',
#             'password2'
#         )


# Registration Form
class RegistrationForm(UserCreationForm):
    """
    This form is for creating new user in database
    """
    phone = forms.CharField(required=True, max_length=11, help_text=_('Required field. For example 09123456789'),
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Username",
                                    "class": "form-control"
                                }
                            ))
    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(
                                 attrs={
                                     "placeholder": "Email",
                                     "class": "form-control"
                                 }
                             ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('phone', 'email', 'password1', 'password2')


# Update Information Of the User Form
class UpdateInfoForm(forms.ModelForm):
    """
    Update user information
    """

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'email']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Change Password Form
class MyPasswordChangeForm(PasswordChangeForm):
    """
    Custom password change form of django
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})


# Address Form
class AddressFrom(forms.ModelForm):
    """
    Form for add an address
    """

    class Meta:
        model = Address
        fields = ['city', 'province', 'detail', 'post_code']
        widgets = {
            'city': forms.TextInput(attrs={"placeholder": _("Tehran"), 'class': 'form-control'}),
            'province': forms.TextInput(attrs={"placeholder": _("Province 2"), 'class': 'form-control'}),
            'detail': forms.TextInput(attrs={"placeholder": _("Vakili Alley, Plaque 12"), 'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={"placeholder": _("1234567890"), 'class': 'form-control'}),
        }


class UpdateAddressForm(forms.ModelForm):
    """
    Update address information
    """

    class Meta:
        model = Address
        fields = ['city', 'province', 'detail', 'post_code']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
