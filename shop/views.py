from django.shortcuts import render
from .models import Shop,Categoriey
from django.core.paginator import Paginator
# Create your views here.

def view_products(request):
    clothes = Shop.objects.all()
    clothes_categ = Categoriey.objects.all()
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

    # count the products size options
    
    context = {"all_clothes" : page_obj,
               "categ_avilable" : l
               }
    return render(request, "shop/view_products.html",context)

def product_details(request, id):
    details = Shop.objects.get(id=id)
    context = {"product" : details}
    return render(request,"shop/product_details.html",context)
