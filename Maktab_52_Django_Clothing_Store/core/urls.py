from django.urls import path

from core.views import *

# Just for test
urlpatterns = [
    path('base/', MyView.as_view(), name='baseview'),
    path('test/', test, name='test'),
    ]
