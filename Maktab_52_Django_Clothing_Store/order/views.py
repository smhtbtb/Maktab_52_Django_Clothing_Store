from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.views.decorators.http import require_POST
# from order.cart import Cart
# from order.forms import CartAddProductForm
from rest_framework import generics

from order.models import Order
from order.permissions import *
from order.serializers import *
from product.models import Product


class CartList(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        # user = User.objects.get(id=request.user.id)
        user = request.user
        # if user.address_set.count() == 0:
        #     return redirect(reverse_lazy('customer:address_create'))
        # items = list(request.COOKIES.get('cart', '').split('-')[:-1])
        items = set(request.COOKIES.get('cart', '').split('-')[:-1])
        order = user.order_set.filter(status__exact='Pr')
        # print(order)
        if order:
            if order.count() == 1:
                # order = order
                order = order.first()
                # print('order: ', order, 'items: ', items)
                for item in items:
                    product = Product.objects.get(id=int(item))
                    if not order.orders.filter(product=product):
                        OrderItem.objects.create(order=order, product=product)

                # Delete
                delete_item = list(request.COOKIES.get('delete', ''))
                if delete_item and delete_item is not None:
                    # print(delete_item[0])
                    delete_product = Product.objects.get(id=int(delete_item[0]))
                    OrderItem.objects.get(order=order, product=delete_product).delete()

                # update qty +
                plus = list(request.COOKIES.get('plus', ''))
                if plus and plus is not None:
                    # print(plus[0])
                    plus_product = Product.objects.get(id=int(plus[0]))
                    plus_item = OrderItem.objects.get(order=order, product=plus_product)
                    plus_item.number += 1
                    plus_item.save()

                # update qty -
                minus = list(request.COOKIES.get('minus', ''))
                if minus and minus is not None:
                    # print(minus[0])
                    minus_product = Product.objects.get(id=int(minus[0]))
                    minus_item = OrderItem.objects.get(order=order, product=minus_product)
                    minus_item.number -= 1
                    minus_item.save()

        else:
            new_order = Order.objects.create(user=user)
            order = new_order
            # print('new order: ', order, 'items: ', items)
            for item in items:
                product = Product.objects.get(id=int(item))
                OrderItem.objects.create(order=order, product=product)

        cart_items = order.orders.all()
        # print(cart_items.count())
        resp = render(request, 'order_temp/detail.html', {
            'order': order,
            'cart_items': cart_items,
            'n': list(range(cart_items.count()))
        })
        resp.set_cookie('delete', '')
        resp.set_cookie('plus', '')
        resp.set_cookie('minus', '')
        resp.set_cookie('cart', '')
        return resp

    # def post(self, request, *args, **kwargs):
    #     resp = JsonResponse({'x': 'y'})
    #     # print(request.POST['plus'])
    #
    #     # resp.set_cookie('delete', request.POST['will_delete'])
    #     resp.set_cookie('plus', request.POST['plus'])
    #     # resp.set_cookie('minus', request.POST['minus'])
    #
    #     # d = request.POST.get("will_delete")
    #     # if d and d is not None:
    #     #     resp.set_cookie('delete', d)
    #     # p = request.POST.get('plus')
    #     # if p and p is not None:
    #     #     resp.set_cookie('plus', p)
    #     # m = request.POST.get('minus')
    #     # if m and m is not None:
    #     #     resp.set_cookie('minus', m)
    #     return resp


# Plus product qty
def plus_product_qty(request, o_i_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    if request.method == 'GET':
        return reverse_lazy('order:cart_list')

    # fetch the object related to passed id
    obj = get_object_or_404(OrderItem, id=o_i_id)

    if request.method == "POST":
        # delete object
        if obj.number < obj.product.leftovers:
            obj.number = F('number') + 1
            obj.save()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect(reverse_lazy('order:cart_list'))

    return render(request, "order_temp/detail.html", context)


# Minus product qty
def minus_product_qty(request, o_i_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    if request.method == 'GET':
        return reverse_lazy('order:cart_list')

    # fetch the object related to passed id
    obj = get_object_or_404(OrderItem, id=o_i_id)

    if request.method == "POST":
        # delete object
        if obj.number > 1:
            obj.number = F('number') - 1
            obj.save()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect(reverse_lazy('order:cart_list'))

    return render(request, "order_temp/detail.html", context)


# Delete from cart
class DeleteCartItem(LoginRequiredMixin, generic.DeleteView):
    model = OrderItem
    success_url = reverse_lazy('order:cart_list')


# Local Storage

# class CartList(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'order_temp/detail.html'


# # Add to cart
# def add_to_cart(request):
#     # del request.session['cartdata']
#     cart_p = {str(request.GET['id']): {
#         'image': request.GET['image'],
#         'name': request.GET['name'],
#         'number': request.GET['number'],
#         'price': request.GET['price'],
#     }}
#     if 'cartdata' in request.session:
#         if str(request.GET['id']) in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             cart_data[str(request.GET['id'])]['number'] = int(cart_p[str(request.GET['id'])]['number'])
#             cart_data.update(cart_data)
#             request.session['cartdata'] = cart_data
#         else:
#             cart_data = request.session['cartdata']
#             cart_data.update(cart_p)
#             request.session['cartdata'] = cart_data
#     else:
#         request.session['cartdata'] = cart_p
#     return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})
#
#
# # Cart List Page
# def cart_list(request):
#     total_amt = 0
#     if 'cartdata' in request.session:
#         for p_id, item in request.session['cartdata'].items():
#             total_amt += int(item['number']) * int(item['price'])
#         return render(request, 'order_temp/detail.html',
#                       {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
#                        'total_amt': total_amt})
#     else:
#         return render(request, 'order_temp/detail.html', {'cart_data': '', 'totalitems': 0, 'total_amt': total_amt})
#
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
    permission_classes = [
        IsSuperUser
    ]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [
        IsSuperUserOrOwner
    ]


class OrderItemListCreateApiView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [
        IsSuperUser
    ]


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [
        IsSuperUserOrOwnerItem
    ]
