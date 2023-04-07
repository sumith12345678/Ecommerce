# from django.db.models import Count
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.views import View
from . models import *
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q




def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


class CategoryView(View):
 def get(self,request,val):
     product = Product.objects.filter(category=val)
     name = Product.objects.filter(category=val).values('name')
    #  price = Product.objects.filter(category=val).values('price')
     return render(request,"category.html",locals())
 
 
class ProductDetailView(View):
 def get(self,request,pk):
     product = Product.objects.get(pk=pk)
     return render(request,"productdetail.html",locals())  
 
 
class CustomerRegistrationView(View):
 def get(self,request):
     form = CustomerRegistrationForm()
     return render(request,"registration.html",locals())
 def post(self,request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
         form.save()
         messages.success(request,"Congratulations! User Registration Successfull")
     else:
         messages.warning(request,"Invalid Input Data")
     return render(request,"registration.html",locals()) 
 
# class PasswordResetView(View):
#  def get(self,request):
#       return render(request,"profile.html",locals()) 
#  def post(self,request):
#      return render(request,"profile.html",locals())
      
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']
            
            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,pincode=pincode)
            reg.save()
            messages.success(request,"Congratulations! User Registration Successfull")
            
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'profile.html',locals())        
            
def address(request):
        add = Customer.objects.filter(user=request.user)
        return render(request,'address.html',locals())
    
class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'Updateaddress.html',locals())
    
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.pincode = form.cleaned_data['pincode']
            add.save()
            messages.success(request,"Congratulations! Ypur Profile Update is Successfull")
        else:
            messages.warning(request,"Invalid Input Data")    
        return redirect("address")
    
    
def add_to_cart(request):
            user =request.user
            product_id=request.GET.get('prod_id')
            product = Product.objects.get(id=product_id)
            Cart(user=user,product=product).save()
            return redirect("/cart")
        
def show_cart(request):
           user =request.user
           cart = Cart.objects.filter(user=user)
           amount = 0
           for p in cart:
               value = p.quantity * p.product.discount_price
               amount = amount + value
           totalamount =amount + 40    
           return render(request,'addtocart.html',locals())
 
class checkout(View):
    def get(self,request):
        user =request.user
        add =Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discount_price
            famount = famount + value
        totalamount = famount + 40    
        return render(request,'checkout.html',locals())
           
                
def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
        totalamount = amount + 40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }    
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
        totalamount = amount + 40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }    
        return JsonResponse(data) 
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
        totalamount = amount + 40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }    
        return JsonResponse(data)     

# # Create your views here.
# .annotate(total=Count('name'))