from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# My contact view
# class ContactView(generic.FormView):
#     form_class = ContactForm
#     template_name = 'contact_temp/contact.html'
#     success_url = reverse_lazy('contact:contact')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, ['mohammad.h_78@yahoo.com', ])
            return render(request, 'contact_temp/success.html')
        else:
            return render(request, 'contact_temp/contact.html', {'form': form, })
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_temp/contact.html', context)
