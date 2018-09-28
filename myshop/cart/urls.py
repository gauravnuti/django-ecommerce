from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.show_cart, {'template_name':'shop/cart/cart.html'}, name = 'show_cart'),
]