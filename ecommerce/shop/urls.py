"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordRestForm,MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
   path('',views.home,name=''),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   
   
   path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
   path('product_detail/<int:pk>',views.ProductDetailView.as_view(),name='product_detail'),
   
   
   
   path('profile/',views.ProfileView.as_view(),name='profile'),
   path('address/', views.address,name='address'),
   path('Updateaddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
   
   path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
   path('cart/', views.show_cart, name='showcart'),
   path('checkout/', views.checkout.as_view(), name='checkout'),
   
   
   path('pluscart/', views.plus_cart, name='plus_cart'),
   path('minuscart/', views.minus_cart, name='minus_cart'),
   path('removecart/', views.remove_cart, name='remove_cart'),
   
    
    
  #login authentication
  path('registration/',views.CustomerRegistrationView.as_view(),name='registration'),
  path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
#   path('password-rest/',auth_view.PasswordResetView.as_view(template_name='password_rest.html',form_class=MyPasswordRestForm),name='password_reset'),
  path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
  path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='changepassworddone.html'),name='passwordchangedone'),
  path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
  
  path('password-rest/', auth_view.PasswordResetView.as_view(template_name='password_rest.html',form_class=MyPasswordRestForm), name='password_reset'),
  
  path('password-rest/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_rest_done.html'), name='password_reset_done'),
   
  path('password-rest-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='password_rest_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
  
  path('password-rest-complete/>', auth_view.PasswordResetCompleteView.as_view(template_name='password_rest_complete.html'), name='password_reset_complete'),
]


