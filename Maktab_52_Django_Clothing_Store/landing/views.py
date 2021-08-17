from django.shortcuts import render

# Create your views here.
from django.views import generic

from product.models import Product


class Landing(generic.TemplateView):
    template_name = 'landing_temp/landing.html'
    extra_context = {
        'products': Product.objects.all()
    }

