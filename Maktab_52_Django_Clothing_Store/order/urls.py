from django.urls import path

from order.views import *

app_name = 'order'
urlpatterns = [
    # Template Views

    # path('p/', product_api),
    # path('', CartDetail, name='cart_detail'),

    path('cart_list', CartList.as_view(), name='cart_list'),
    path('cart_delete/<int:pk>', DeleteCartItem.as_view(), name='cart_delete'),
    path('plus_product_qty/<o_i_id>', plus_product_qty, name='plus_product_qty'),
    path('minus_product_qty/<o_i_id>', minus_product_qty, name='minus_product_qty'),
    path('update_address/<a_id>', update_address, name='update_address'),
    path('delete_address_order/<o_id>', delete_address_order, name='delete_address_order'),

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
