from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

#from myshop.checkout.models import Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request,SSL,template_name = "registration/register.html"):
	if request.method == 'POST':
		postdata = request.POST.copy()
		form = UserCreationForm(postdata)
		if form.is_valid():
			form.save()
			un = postdata.get('username','')
			pw = postdata.get('password1','')
			from django.contrib.auth import login, authenticate
			new_user = authenticate(username = un, password = pw)
			if new_user and new_user.is_active:
				login(request, new_user)
				url = reverse('my_account')
				return HttpResponseRedirect(url)
	else:
		form = UserCreationForm()
	page_title = 'User Registration'
	return render(request,template_name,locals())

@login_required
def my_account(request, template_name="registration/my_account.html"):
	page_title = 'My Account'
	#orders = Order.objects.filter(user = request.user)
	name = request.user.username
	return render(request,template_name,locals())

# @login_required
# def order_details(request, order_id, template_name="registration/order_details.html"):
#     """ displays the details of a past customer order; order details can only be loaded by the same 
#     user to whom the order instance belongs.
    
#     """
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     page_title = 'Order Details for Order #' + order_id
#     order_items = OrderItem.objects.filter(order=order)
#     return render_to_response(template_name, locals(), context_instance=RequestContext(request))

	
