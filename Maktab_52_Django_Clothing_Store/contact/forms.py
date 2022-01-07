from django import forms
from django.utils.translation import gettext_lazy as _
from contact.models import Contact
from captcha.fields import CaptchaField


# The contact form
class ContactForm(forms.ModelForm):
    """
    Update address information
    """
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']
        widgets = {
            'email': forms.TextInput(attrs={"placeholder": _("your_email@gmail.com"), 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={"placeholder": _("The subject"), 'class': 'form-control'}),
            'message': forms.Textarea(
                attrs={"placeholder": _("Write your message"), 'class': 'form-control', 'cols': "30", 'rows': "10"}),
            'captcha': forms.TextInput(attrs={"placeholder": _("Captcha"), 'class': 'form-control'}),
        }
