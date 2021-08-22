from django.conf import settings
from product.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        # self.cupon_id = self.session.get('cupon_id')
        # cart = self.session.get(settings.CART_SESSION_ID)
        cart = {}
        if not cart:
            cart = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    # @property
    # def cupon(self):
    #     if self.cupon_id:
    #         return Cupon.objects.get(id=self.cupon_id)
    #     return None
    #
    # def get_discount(self):
    #     if self.cupon:
    #         return (self.cupon.discount / int('100')) * self.get_total_price()
    #     return int('0')
    #
    # def get_total_price_after_discount(self):
    #     return self.get_total_price() - self.get_discount()
