from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from django.views.generic import TemplateView


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


class MyLoginView(LoginView):
    pass


class ProfileView(PermissionRequiredMixin, TemplateView):
    permission_required = 'auth.see_profile'
    template_name = 'customer_temp/profile-datail.html'


class MyLogoutView(LogoutView):
    pass




