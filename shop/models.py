from django.db import models
from django.utils.text import slugify
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


def customize_image(instance, file_name):
    sep = file_name.split(".")
    return "product/%s.%s"%(instance.id, sep[1])


class Shop(models.Model):  # --> table 
    
    product_name = models.CharField(max_length=20) # --> column
    product_price = models.IntegerField()
    product_size = models.CharField(max_length=10,choices=SIZE_OPTIONS)
    product_color = models.CharField(max_length=10,choices=COLOR_OPTIONS)
    categories = models.ForeignKey('Categoriey',on_delete=models.CASCADE)
    product_description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=customize_image)
    vendor_name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Shop,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name
    
class Categoriey(models.Model):
    name =  models.CharField(max_length=10) 
    def __str__(self):
        return self.name

class VendorAdd(models.Model):
    add_prod_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    vendor_email = models.EmailField()
    product_images = models.ImageField(upload_to='vendor_images/')
    product_description = models.TextField(max_length=1000)
    product_price = models.IntegerField()
    product_categ = models.ForeignKey(Categoriey, on_delete=models.CASCADE, related_name='prod_categ')
    created_at = models.DateTimeField(auto_now=True)
    # amount of this product and it's color 
    
    def __str__(self):
        return self.add_prod_name
    
