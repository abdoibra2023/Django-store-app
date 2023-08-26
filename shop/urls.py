from django.urls import path, include
from .views import view_products, product_details

app_name = 'shop'

urlpatterns = [
    path('', view_products),
    path('<int:id>', product_details, name='details'),
]
