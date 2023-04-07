from django.db import models
from django.contrib.auth.models import User



    
    
    
class Product(models.Model):
    CATEGORY = (
        ('Sm', 'Smart'),
        ('Di', 'Digital'),
        ('An', 'Analog'),
        ('Sp', 'Sports'),
        ('Qu', 'Quartz'),
        ('Ch', 'Chronograph'),
           
    )
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    discount_price=models.FloatField(null=True)
    description=models.TextField(null=True)
    
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    stock =models.IntegerField()
    
  
        
    def __str__(self):
        return self.name 
    
class Customer(models.Model):
    STATE_CHOICES = (
        ('Kerala', 'Kerala'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Assam', 'Assam'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Bihar', 'Bihar'),
        ('Haryana', 'Haryana'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('Rajasthan', 'Rajasthan'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Nagaland', 'Nagaland'),
        ('Sikkim', 'Sikkim'),
        ('Manipur', 'Manipur'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Odisha', 'Odisha'),
        ('Goa', 'Goa'),
        ('Karnataka', 'Karnataka'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Gujarat', 'Gujarat'),
        ('Mizoram', 'Mizoram'),
        ('Tripura', 'Tripura'), 
        ('West Bengal', 'West Bengal'),
        ('Jharkhand', 'Jharkhand'),
        ('Meghalaya', 'Meghalaya'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),

                  
       

        
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField (max_length=200, null=True)
    locality = models.CharField (max_length=200, null=True)
    city = models.CharField(max_length=50,null=True)
    mobile = models.IntegerField(default=0)
    pincode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100,null=True)

    def __str__(self):
        return self.name
       
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price   
    
 
 
STATUS_CHOICES = (
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On The way' , 'On The way'),
    ('Delivered' , 'Delivered'),
    ('Cancel' , 'Cancel'),
    ('Pending' , 'Pending'),
) 
 
 


# Create your models here.
