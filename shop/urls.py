from django.urls import path, include
from .views import view_products, product_details, add_product

app_name = 'shop'

urlpatterns = [
    path('', view_products, name='view_all'),
    path('vendor-info', add_product, name='vendor-details'),
    path('<str:slug>', product_details, name='details'),
]
