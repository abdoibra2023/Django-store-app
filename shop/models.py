from django.db import models

# Create your models here.
SIZE_OPTIONS = (
    ("small","small"),
    ("meduiem","meduiem"),
    ("large","large"),
)

COLOR_OPTIONS = (
    ("red","red"),
    ("green","green"),
    ("blue","blue"),
    ("purple","purple"),

)

CATEGORIEY = (
    ("men","men"),
    ("women","women"),
    ("children","children"),

)

class Shop(models.Model):  # --> table
    product_title = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_size = models.CharField(max_length=10,choices=SIZE_OPTIONS)
    product_color = models.CharField(max_length=10,choices=COLOR_OPTIONS)
    categories = models.CharField(max_length=10,choices=CATEGORIEY)

    def __str__(self):
        return self.product_title