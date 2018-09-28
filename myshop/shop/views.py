from django.shortcuts import get_object_or_404, render_to_response, render
from .models import Category, Product
from django.template import RequestContext
from shop.forms import ProductAddToCartForm
from django.urls import reverse
from cart import cart
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import cache
from myshop.settings import CACHE_TIMEOUT
from django.db.models import Q
# Create your views here.
def product_list(request, category_slug = None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(availble = True)
	if category_slug:
		category = get_object_or_404(Category,slug= category_slug)
		products = products.filter(category = category)
	return render(request,'shop/products/list1.html',{'category' : category,
													'categories':categories,
													'products':products})

# def product_detail(request, id, slug):
# 	product = get_object_or_404(Product,id = id, slug = slug, availble = True)
# 	cart_product_form = CartAddProductForm()
# 	return render(request,'shop/products/detail.html',{'product':product,'cart_product_form':cart_product_form})

def product_detail(request, id, slug, template_name="shop/products/details1.html"):
    """ view for each product page """
    product_cache_key = request.path
    # try to get product from cache
    p = cache.get(product_cache_key)
    # if a cache miss, fall back on db query
    if not p:
        p = get_object_or_404(Product, slug=slug, availble = True)
        # store item in cache for next time
        cache.set(product_cache_key, p, CACHE_TIMEOUT)
    #categories = p.categories.filter(is_active=True)
    #page_title = p.name
    #meta_keywords = p.meta_keywords
    #meta_description = p.meta_description
    # evaluate the HTTP method, change as needed
    if request.method == 'POST':
        #create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #print("hrllo")
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        #create the unbound form. Notice the request as a keyword argument
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = slug
    # set test cookie to make sure cookies are enabled
    request.session.set_test_cookie()
    #stats.log_product_view(request, p)
    # product review additions, CH 10
    #product_reviews = ProductReview.approved.filter(product=p).order_by('-date')
    #review_form = ProductReviewForm()
    return render(request,'shop/products/details1.html',{'product':p, 'form':form})

def results(request):
	search_text = request.GET.get('q','')
	category = None
	categories = Category.objects.all()
	results = Product.objects.filter(name__icontains = search_text)
	return render(request,'shop/products/list1.html',{'category' : category,
													'categories':categories,
													'products':results})
