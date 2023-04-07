from django.contrib import admin
from . models import *


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','image','stock')
 

 
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','quantity')   
    
    

           

# Register your models here.
