from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import generic
# Create your views here.
from rest_framework import generics
from django.utils.translation import gettext_lazy as _

from product.models import Product
from product.permissions import IsSuperUser, IsSuperUserOrNot
from product.serializers import *


class ProductDetail(generic.DetailView):
    template_name = 'product_temp/product_detail_view.html'
    model = Product
    context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        resp = JsonResponse({'x': 'y'})
        cart = request.COOKIES.get('cart', '')
        resp.set_cookie('cart', cart + request.POST['products'] + '-')
        return resp


class ProductCardView(generic.DetailView):
    template_name = 'product_temp/product_card_view.html'
    model = Product
    context_object_name = 'product'


class ProductIndexView(generic.TemplateView):
    template_name = 'product_temp/product_index.html'
    extra_context = {
        'products': Product.objects.all()
    }


class ProductMenView(generic.TemplateView):
    template_name = 'product_temp/product_index_men.html'
    extra_context = {
        'products': Product.objects.filter(category__parent__name='men')
    }


class ProductWomenView(generic.TemplateView):
    template_name = 'product_temp/product_index_women.html'
    extra_context = {
        'products': Product.objects.filter(category__parent__name='women')
    }


class ProductChildrenView(generic.TemplateView):
    template_name = 'product_temp/product_index_children.html'
    extra_context = {
        'products': Product.objects.filter(category__parent__name='children')
    }


def scookie(request):
    response = HttpResponse('cookie')
    response.set_cookie('x', 'y')
    return response


def gcookie(request):
    my_y = request.COOKIES['x']
    return HttpResponse('this is my y: ' + my_y)


def addcookie(request):
    resp = HttpResponse('successfully added to cart')
    cart = request.COOKIES.get('cart', '')
    resp.set_cookie('cart', cart + 'zzz')
    # resp.set_cookie('cart', cart + request.POST['zzz'] + ',')
    return resp


def test_cookie(request):
    if not request.COOKIES.get('cart'):
        response = HttpResponse("Visiting for the first time.")
        response.set_cookie('cart', '2,3,4,')
        return response
    else:
        return HttpResponse(f"Your favorite cart is {request.COOKIES['cart']}")

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
    permission_classes = [
        IsSuperUserOrNot
    ]


class ProductMenListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(category__parent__name='men')
    permission_classes = [
        IsSuperUserOrNot
    ]


class ProductWomenListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(category__parent__name='women')
    permission_classes = [
        IsSuperUserOrNot
    ]


class ProductChildrenListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(category__parent__name='children')
    permission_classes = [
        IsSuperUserOrNot
    ]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [
        IsSuperUserOrNot
    ]


class BrandListCreateApiView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [
        IsSuperUserOrNot
    ]


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    permission_classes = [
        IsSuperUserOrNot
    ]


class CategoryListCreateApiView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [
        IsSuperUserOrNot
    ]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [
        IsSuperUserOrNot
    ]


class DiscountListCreateApiView(generics.ListCreateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [
        IsSuperUser
    ]


class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [
        IsSuperUser
    ]
