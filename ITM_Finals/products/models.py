from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=250, help_text = "Enter product category.")
    
    class Meta:
        ordering = ('category_name',)
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250, help_text = "Enter product name.")
    description = models.TextField(blank=True, null=True, help_text = "Enter product description.") 
    price = models.FloatField(help_text = "Enter product price.")
    image = models.ImageField(upload_to='product_images', blank=True, null=True, help_text = "Upload product image.")
    available = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ('-publish_date',)
        
    def __str__(self):
        return self.product_name
    
    