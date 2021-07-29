from django.contrib import admin
from django.urls import path, include

from customer.views import *

app_name = 'customer'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login_page'),
    path('profile_detail/', ProfileView.as_view(), name='profile_detail'),
    path('logout/', MyLogoutView.as_view(), name='logout_page'),

]

