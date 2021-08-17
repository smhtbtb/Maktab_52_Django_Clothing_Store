from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
# from order.cart import Cart
# from order.forms import CartAddProductForm
from rest_framework import generics

from order.models import Order
from order.serializers import *
from product.models import Product


# @require_POST
# def CartAdd(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('order:cart_detail')
#
#
# def CartRemove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('order:cart_detail')
#
#
# def CartDetail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(
#             initial={
#                 'quantity': item['quantity'],
#                 'update': True
#             })
#     # cupon_apply_form = CuponApllyForm()
#     return render(request, 'order_temp/detail2.html', {'cart': cart})

# Add to cart
def add_to_cart(request):
    # del request.session['cartdata']
    cart_p = {str(request.GET['id']): {
        'image': request.GET['image'],
        'name': request.GET['name'],
        'number': request.GET['number'],
        'price': request.GET['price'],
    }}
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[str(request.GET['id'])]['number'] = int(cart_p[str(request.GET['id'])]['number'])
            cart_data.update(cart_data)
            request.session['cartdata'] = cart_data
        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata'] = cart_data
    else:
        request.session['cartdata'] = cart_p
    return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})


# Cart List Page
def cart_list(request):
    total_amt = 0
    if 'cartdata' in request.session:
        for p_id, item in request.session['cartdata'].items():
            total_amt += int(item['number']) * int(item['price'])
        return render(request, 'order_temp/detail.html',
                      {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
                       'total_amt': total_amt})
    else:
        return render(request, 'order_temp/detail.html', {'cart_data': '', 'totalitems': 0, 'total_amt': total_amt})

# # Delete Cart Item
# def delete_cart_item(request):
#     p_id = str(request.GET['id'])
#     if 'cartdata' in request.session:
#         if p_id in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             del request.session['cartdata'][p_id]
#             request.session['cartdata'] = cart_data
#     total_amt = 0
#     for p_id, item in request.session['cartdata'].items():
#         total_amt += int(item['qty']) * float(item['price'])
#     t = render_to_string('ajax/cart-list.html',
#                          {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
#                           'total_amt': total_amt})
#     return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})
#
#
# # Update Cart Item
# def update_cart_item(request):
#     p_id = str(request.GET['id'])
#     p_qty = request.GET['qty']
#     if 'cartdata' in request.session:
#         if p_id in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             cart_data[str(request.GET['id'])]['qty'] = p_qty
#             request.session['cartdata'] = cart_data
#     total_amt = 0
#     for p_id, item in request.session['cartdata'].items():
#         total_amt += int(item['qty']) * float(item['price'])
#     t = render_to_string('ajax/cart-list.html',
#                          {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
#                           'total_amt': total_amt})
#     return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})


####################################################################################################################

# TODO Api View

class OrderListCreateApiView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class OrderItemListCreateApiView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = Order.objects.all()

