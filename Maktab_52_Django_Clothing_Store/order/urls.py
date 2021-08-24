from django.urls import path

from order.views import *

app_name = 'order'
urlpatterns = [
    # Template Views

    # path('p/', product_api),
    # path('', CartDetail, name='cart_detail'),

    path('cart_list', CartList.as_view(), name='cart_list'),

    # path('add-to-cart', add_to_cart, name='add_to_cart'),
    # path('cart', cart_list, name='cart'),

    # path('delete-from-cart', delete_cart_item, name='delete-from-cart'),
    # path('update-cart', update_cart_item, name='update-cart'),

    # Api Views

    path('orders_listcreate', OrderListCreateApiView.as_view(), name='api_orders_listcreate'),
    path('orders_detail_view/<int:pk>', OrderDetailView.as_view(), name='api_orders_detail_view'),

    path('order_item_listcreate', OrderItemListCreateApiView.as_view(), name='api_order_item_listcreate'),
    path('order_item_detail_view/<int:pk>', OrderItemDetailView.as_view(), name='api_order_item_detail_view'),

]
