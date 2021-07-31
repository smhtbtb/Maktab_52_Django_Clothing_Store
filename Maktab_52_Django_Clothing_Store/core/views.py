from django.shortcuts import render

# Create your views here.

from django.views import generic


class MyView(generic.TemplateView):
    template_name = 'base_temp/base.html'
