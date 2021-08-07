from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import *
from product.views import *

app_name = 'product'
urlpatterns = [
    # path('p/', product_api),
    path('product_card_view/<int:pk>', ProductCardView.as_view(), name='product_card_view'),

    path('products_listcreate', ProductListCreateApiView.as_view()),
    path('products_detail_view/<int:pk>', ProductDetailView.as_view()),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
