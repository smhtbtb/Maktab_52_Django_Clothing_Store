from django.urls import path
from contact.views import *

app_name = 'contact'
urlpatterns = [
    # Template Views
    # path('', ContactView.as_view(), name='contact'),
    path('', contact_view, name='contact'),
]
