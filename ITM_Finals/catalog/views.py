from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .models import *
from products.models import Category, Product
from quotation.models import ShippingAddress

from .forms import SignupForm, LoginForm 


def index(request):
    products = Product.objects.filter(available=True)[0:9]
    
    return render(request, 'catalog/index.html', {
        'products' : products,
    }
)
    
def contact(request):
    return render(request, 'catalog/contact.html')

def terms(request):
    return render(request, 'catalog/terms.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        form = SignupForm()
    
    return render(request, 'catalog/signup.html', {
        'form': form
    })
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('catalog/index.html', {
                'form' : form
            })
    
    else:
        form = LoginForm()

def logout_view(request):
    logout(request)
    return render(request, 'catalog/logout.html')

def my_dashboard(request):
    return render(request, 'catalog/my_dashboard.html')
