from django.conf.urls import url
from myshop import settings
from . import views
from django.urls import path

urlpatterns = [
	url(r'^register/$', views.register, 
	    {'template_name': 'registration/register.html', 'SSL': True }, 'register'),
	url(r'^my_account/$', views.my_account, 
		{'template_name': 'registration/my_account.html'}, 'my_account'),
	# url(r'^order_info/$', 'order_info', 
	# 	{'template_name': 'registration/order_info.html'}, 'order_info'),
	# url(r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details', 
	# 	{'template_name': 'registration/order_details.html'}, 'order_details'),
]

from django.contrib.auth import views as auth_views
urlpatterns += [
	path('login/', auth_views.login,
		{'template_name': 'registration/login.html', 'extra_context' : {'SSL': True } },name = 'login'),
	# path('logout/', auth_views.logout, 
	#  {'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL }, 'logout'),
	# path('password_change/', auth_views.login, 
	#  {'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL }, 'login'),
]
