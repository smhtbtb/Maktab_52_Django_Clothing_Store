from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView

from customer.views import *
from django.contrib.auth import views

app_name = 'customer'
urlpatterns = [
    # Template Views
    path('login/', MyLoginView.as_view(), name='login'),
    path('profile_detail/', ProfileView.as_view(), name='profile_detail'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer_temp/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('address_list/', AddressListView.as_view(), name='address_list'),
    path('address_create/', AddressCreateView.as_view(), name='address_create'),
    path('address_update/<int:pk>', AddressUpdateView.as_view(), name='address_update'),
    path('address_delete/<int:pk>', AddressDeleteView.as_view(), name='address_delete'),
    path('update_info/<int:pk>', UpdateInfo.as_view(), name='update_info'),
    path('change_password/', MyPasswordChangeView.as_view(), name='change_password'),
    path('shopping_history/', ShoppingHistory.as_view(), name='shopping_history'),
    path('shopping_details/<int:pk>', ShoppingDetails.as_view(), name='shopping_details'),


    # API Views
    path('users_list/', UserListApi.as_view(), name='users_list'),
    path('user_detail/<int:pk>', UserDetailApi.as_view(), name='user_detail'),

    path('addresses_list/', AddressListApi.as_view(), name='addresses_list'),
    path('address_detail/<int:pk>', AddressDetailApi.as_view(), name='address_detail'),

    path('api_login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api_login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_register/', RegisterView.as_view(), name='auth_register'),
    path('api_logout/', user_logout, name='auth_logout'),

]
