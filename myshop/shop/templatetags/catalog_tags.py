from django import template
from cart import cart
from shop.models import Category

register = template.Library()

@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
	cart_item_count = cart.cart_distinct_item_count(request)
	return {'cart_item_count' : cart_item_count }

@register.inclusion_tag("tags/categories.html")
def categories1(request):
	categories = Category.objects.all()
	return {'categories' : categories}