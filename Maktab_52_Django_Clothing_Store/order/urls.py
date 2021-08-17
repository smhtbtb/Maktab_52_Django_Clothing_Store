from django.urls import path

from order.views import *

app_name = 'order'
urlpatterns = [
    # Template Views

    # path('p/', product_api),
    # path('', CartDetail, name='cart_detail'),
    path('add-to-cart', add_to_cart, name='add_to_cart'),
    path('cart', cart_list, name='cart'),
    # path('delete-from-cart', delete_cart_item, name='delete-from-cart'),
    # path('update-cart', update_cart_item, name='update-cart'),

    # Api Views

    path('orders_listcreate', OrderListCreateApiView.as_view(), name='api_orders_listcreate'),

]
