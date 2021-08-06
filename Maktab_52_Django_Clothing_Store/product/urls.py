from django.urls import path

from core.views import *
from product.views import *

app_name = 'product'
urlpatterns = [
    # path('p/', product_api),
    path('products_listcreate', ProductListCreateApiView.as_view()),
    path('products_detail_view/<int:pk>', ProductDetailView.as_view()),
]
