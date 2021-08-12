from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from customer.views import *
from django.contrib.auth import views

app_name = 'customer'
urlpatterns = [
    # path('login/', MyLoginView.as_view(), name='login_page'),
    path('login/', views.LoginView.as_view(template_name="customer_temp/login.html", authentication_form=UserLoginForm),
         name='login'),
    path('profile_detail/', ProfileView.as_view(), name='profile_detail'),
    # path('logout/', MyLogoutView.as_view(), name='logout_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer_temp/logout.html'), name='logout'),
    path('register/', register, name='register'),
    # path('register/', Register.as_view(), name='register'),
    path('address_create/', AddressCreateView.as_view(), name='address_create'),



    # TODO API
    path('users_list/', UserListApi.as_view(), name='users_list'),
    path('user_detail/', UserDetailApi.as_view(), name='user_detail'),

    path('addresses_list/', AddressListApi.as_view(), name='addresses_list'),
    path('address_detail/<int:pk>', AddressDetailApi.as_view(), name='address_detail'),

]
