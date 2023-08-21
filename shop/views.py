from django.shortcuts import render
from .models import Shop

# Create your views here.
def view_products(request):
    clothes = Shop.objects.all()
    context = {"all_clothes" : clothes}
    return render(request, "shop/view_products.html",context)

def product_details(request, id):
    details = Shop.objects.get(id=id)
    context = {"product" : details}
    return render(request,"shop/product_details.html",context)