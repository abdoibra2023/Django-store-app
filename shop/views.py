from django.shortcuts import render
from .models import Shop, Categoriey, VendorAdd
from .forms import VendorAddForm
from django.core.paginator import Paginator
# Create your views here.

def view_products(request):
    clothes = Shop.objects.all()
    clothes_categ = Categoriey.objects.all()

    # this part for pagination 
    pagination = Paginator(clothes, 1)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)

    # count the avilable categorey 
    l = {}
    for prod_categ in clothes_categ:
        counter = 0
        for prodct in clothes:
            if prodct.categories == prod_categ:
                counter += 1
        l[str(prod_categ)] = counter
 
    context = {"all_clothes" : page_obj,
               "categ_avilable" : l   # count the avilable categ
               }
    return render(request, "shop/view_products.html", context)

def product_details(request, slug):
    details = Shop.objects.get(slug=slug)
    context = {"product" : details}
    return render(request,"shop/product_details.html", context)


def add_product(request):
    if request.method == 'POST':
        form = VendorAddForm(request.POST, request.FILES)
        if form.is_valid():
            this_form = form.save()
    else:
        form = VendorAddForm()

    context = {"forms" : form}
    return render(request, "shop/add_product.html", context)