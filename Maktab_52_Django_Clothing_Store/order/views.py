from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.views.decorators.http import require_POST
from rest_framework import generics
from order.models import Order
from order.permissions import *
from order.serializers import *
from product.models import Product


class CartList(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.address_set.count() == 0:
            return redirect(reverse_lazy('customer:address_create'))
        items = set(request.COOKIES.get('cart', '').split('-')[:-1])
        order = user.order_set.filter(status__exact='Pr')
        if order:
            if order.count() == 1:
                order = order.first()
                for item in items:
                    product = Product.objects.get(id=int(item))
                    if not order.orders.filter(product=product):
                        OrderItem.objects.create(order=order, product=product)

        else:
            new_order = Order.objects.create(user=user)
            order = new_order
            for item in items:
                product = Product.objects.get(id=int(item))
                OrderItem.objects.create(order=order, product=product)

        cart_items = order.orders.all()

        addresses = user.address_set.all()
        # print(addresses)

        resp = render(request, 'order_temp/detail.html', {
            'order': order,
            'cart_items': cart_items,
            'addresses': addresses,
            'n': list(range(cart_items.count()))
        })
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
        # add object
        if obj.number < obj.product.leftovers:
            obj.number = F('number') + 1
            obj.save()
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
        # remove object
        if obj.number > 1:
            obj.number = F('number') - 1
            obj.save()
        return HttpResponseRedirect(reverse_lazy('order:cart_list'))

    return render(request, "order_temp/detail.html", context)


# Update address
def update_address(request, a_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    if request.method == 'GET':
        return reverse_lazy('order:cart_list')

    # fetch the object related to passed id
    obj = get_object_or_404(Address, id=a_id)

    if request.method == "POST":
        # remove object
        user = request.user
        order = Order.objects.filter(user=user).last()
        order.address = obj
        order.save()
        return HttpResponseRedirect(reverse_lazy('order:cart_list'))

    return render(request, "order_temp/detail.html", context)


# Update address to null
def delete_address_order(request, o_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    if request.method == "POST":
        # remove object
        obj = Order.objects.filter(id=o_id).update(address=None)
        return HttpResponseRedirect(reverse_lazy('order:cart_list'))

    return render(request, "order_temp/detail.html", context)


# Delete from cart
class DeleteCartItem(LoginRequiredMixin, generic.DeleteView):
    model = OrderItem
    success_url = reverse_lazy('order:cart_list')


# TODO
class Checkout(LoginRequiredMixin, generic.UpdateView):
    model = Order
    form_class = ...


####################################################################################################################

# Api View

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
