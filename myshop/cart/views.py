from django.shortcuts import render, get_object_or_404
from cart import cart
from django.template import RequestContext
from django.http import HttpResponseRedirect
from checkout import checkout
from myshop import settings

# Create your views here.

def show_cart(request,template_name = "shop/cart/cart.html"):
	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			cart.remove_from_cart(request)
		if postdata['submit'] == 'Update':
			cart.update_cart(request)
		if postdata['submit'] == 'Checkout':
			checkout_url = checkout.get_checkout_url(request)
			return HttpResponseRedirect(checkout_url)
	cart_items = cart.get_cart_items(request)
	page_title = 'Shopping Cart'
	cart_subtotal = cart.cart_subtotal(request)
	merchant_id = settings.GOOGLE_CHECKOUT_MERCHANT_ID
	return render(request,template_name,locals())