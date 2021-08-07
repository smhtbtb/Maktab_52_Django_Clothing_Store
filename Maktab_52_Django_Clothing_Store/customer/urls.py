from django.contrib import admin
from django.urls import path, include

from customer.views import *
from django.contrib.auth import views

app_name = 'customer'
urlpatterns = [
    # path('login/', MyLoginView.as_view(), name='login_page'),
    path('login/', views.LoginView.as_view(template_name="customer_temp/login.html", authentication_form=UserLoginForm),
         name='login'),
    path('profile_detail/', ProfileView.as_view(), name='profile_detail'),
    path('logout/', MyLogoutView.as_view(), name='logout_page'),

    path('users_list/', UserListApi.as_view(), name='users_list'),
    path('user_detail/', UserDetailApi.as_view(), name='user_detail'),

    path('addresses_list/', AddressListApi.as_view(), name='addresses_list'),
    path('address_detail/<int:pk>', AddressDetailApi.as_view(), name='address_detail'),

]
