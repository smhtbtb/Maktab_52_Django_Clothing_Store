from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


class ProductDetail(generic.DetailView):
    pass


class ProductCardView(generic.DetailView):
    template_name = 'product_temp/product_card_view.html'
    model = Product
    context_object_name = 'product'


class ProductIndexView(generic.TemplateView):
    template_name = 'product_temp/product_index.html'
    extra_context = {
        'products': Product.objects.all()
    }


# __________________________________________________________________________________
# TODO REST API

# @api_view(["POST"])
# @csrf_exempt
# def product_api(request):
#     if request.method == 'GET':
#         p = Product.objects.all()
#         res = ProductSerializer(p, many=True)
#         return JsonResponse({
#             'products': res.data
#         })
#     elif request.method == 'POST':
#         res = ProductSerializer(data=request.data)
#         if res.is_valid():
#             res.save()
#             return JsonResponse(res.data)
#         else:
#             return JsonResponse(res.errors)

class ProductListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


from rest_framework import mixins


# class ProductDetailView(mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         mixins.RetrieveModelMixin,
#                         generics.GenericAPIView):
#
#     def get(self, request, *args, **kwargs):
#         p = Product.objects.get(id=kwargs['pk'])
#         res = ProductSerializer(p)
#         return JsonResponse({
#             'products': res.data
#         })
#
#     def perform_update(self, serializer):
#         serializer.save()
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def perform_destroy(self, instance):
#         instance.delete_it()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # lookup_url_kwarg = 'product_name'
    # lookup_field = 'name'
