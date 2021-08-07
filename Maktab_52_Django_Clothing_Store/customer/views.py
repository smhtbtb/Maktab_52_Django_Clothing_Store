from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from django.views.generic import TemplateView
from rest_framework import generics, permissions

# Create your views here.


# def login_page(request):
#     if request.method == 'POST':
#         u = request.POST['username']
#         p = request.POST['password']
#         user = authenticate(request, username=u, password=p)
#         if user:
#             login(request, user)
#             print(u, p)
#             # return render(request, 'customer_temp/profile-datail.html', {'user': User.objects.get(username=u)})
#             return redirect('customer:profile_detail')
#         else:
#             return render(request, 'customer_temp/login.html')
#     else:
#         return render(request, 'customer_temp/login.html')
#
#
# from customer.forms import LoginUser
#
#
# class Login(generic.FormView):
#     template_name = 'customer_temp/login.html'
#     form_class = LoginUser
#     success_url = reverse_lazy('customer:profile_detail')
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#
# # @login_required
# @permission_required('auth.see_profile')
# def profile_detail(request):
#     return render(request, 'customer_temp/profile-datail.html')
from customer.permissions import IsSuperUser, IsOwner
from customer.serializers import *


class MyLoginView(LoginView):
    pass


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))


class ProfileView(LoginRequiredMixin, TemplateView):
    # permission_required = 'auth.see_profile'
    template_name = 'customer_temp/profile-datail.html'


class MyLogoutView(LogoutView):
    pass


# ______________________________________________________________________________
# API

class UserListApi(generics.ListAPIView):
    serializer_class = UserBriefSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsSuperUser
    ]


class UserDetailApi(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


class AddressListApi(generics.ListAPIView):
    serializer_class = AddressBriefSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Address.objects.filter(owner=self.request.user)


class AddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [
        IsOwner
    ]
