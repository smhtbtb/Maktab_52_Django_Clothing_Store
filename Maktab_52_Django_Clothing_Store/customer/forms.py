from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _

from customer.models import *


class LoginUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


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

class RegistrationForm(UserCreationForm):
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


# class UpdateInfoForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['phone', 'first_name', 'last_name', 'email']
#         widgets = {
#                   'phone': forms.TextInput(attrs={'class': 'form-control'}),
#                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#                   'email': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'email']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     password = self.fields.get('password')
    #     if password:
    #         password.help_text = password.help_text.format('../password/')
    #     user_permissions = self.fields.get('user_permissions')
    #     if user_permissions:
    #         user_permissions.queryset = user_permissions.queryset.select_related('content_type')


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})


class AddressFrom(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'province', 'detail', 'post_code']
        widgets = {
            'city': forms.TextInput(attrs={"placeholder": _("Tehran"), 'class': 'form-control'}),
            'province': forms.TextInput(attrs={"placeholder": _("Province 2"), 'class': 'form-control'}),
            'detail': forms.TextInput(attrs={"placeholder": _("Vakili Alley, Plaque 12"), 'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={"placeholder": _("1234567890"), 'class': 'form-control'}),
        }
