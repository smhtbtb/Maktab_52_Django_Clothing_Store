from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import *
from product.views import *

app_name = 'product'
urlpatterns = [
    # Template Views
    path('', ProductIndexView.as_view(), name='product_index_view'),
    path('men/', ProductMenView.as_view(), name='product_men_view'),
    path('women/', ProductWomenView.as_view(), name='product_women_view'),
    path('children/', ProductChildrenView.as_view(), name='product_children_view'),
    path('product_card_view/<int:pk>', ProductCardView.as_view(), name='product_card_view'),
    path('product_detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),

    # Api Views
    path('products_listcreate', ProductListCreateApiView.as_view(), name='api_products_listcreate'),
    path('products_men_listcreate', ProductMenListCreateApiView.as_view(), name='api_products_men_listcreate'),
    path('products_women_listcreate', ProductWomenListCreateApiView.as_view(), name='api_products_women_listcreate'),
    path('products_children_listcreate', ProductChildrenListCreateApiView.as_view(),
         name='api_products_children_listcreate'),
    path('product_detail_view/<int:pk>', ProductDetailView.as_view(), name='api_product_detail_view'),

    path('brands_listcreate', BrandListCreateApiView.as_view(), name='api_brands_listcreate'),
    path('brand_detail_view/<str:name>', BrandDetailView.as_view(), name='api_brand_detail_view'),

    path('categories_listcreate', CategoryListCreateApiView.as_view(), name='api_categories_listcreate'),
    path('category_detail_view/<int:pk>', CategoryDetailView.as_view(), name='api_category_detail_view'),

    path('discounts_listcreate', DiscountListCreateApiView.as_view(), name='api_discounts_listcreate'),
    path('discount_detail_view/<int:pk>', DiscountDetailView.as_view(), name='api_discount_detail_view'),

]
