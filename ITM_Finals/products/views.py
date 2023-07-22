from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category
from .forms import NewItemForm, EditItemForm

def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category',0)
    sort_param = request.GET.get('sort')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_id:
        products = products.filter(category_id=category_id)
        
    if query:
        products = products.filter(Q(product_name__icontains=query) | Q(description__icontains=query))
    
    if sort_param == 'alpha':
        products = products.order_by('product_name')
    elif sort_param == 'price':
        products = products.order_by('price')
    elif sort_param == 'latest':
        products = products.order_by('-publish_date')
    
    return render(request, 'products/browse.html', {
        'products' : products,
        'query' : query,
        'categories' : categories,
        'category_id' : category_id,
        'sort_param' : sort_param,
    })

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(pk=pk)[:3]
    
    return render(request, 'products/detail.html', {
        'product': product,
        'related_products': related_products,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            
            return redirect('product:detail', pk=product.id)
    else:
        form = NewItemForm()
    
    return render(request, 'products/form.html',{
        'form': form,
        'title': 'New item',
    })

@login_required
def manage(request):
    products = Product.objects.all()
    query = request.GET.get('query', '')
    category_id = request.GET.get('category',0)
    sort_param = request.GET.get('sort')
    categories = Category.objects.all()
    
    if category_id:
        products = products.filter(category_id=category_id)
        
    if query:
        products = products.filter(Q(product_name__icontains=query) | Q(description__icontains=query))
    
    if sort_param == 'alpha':
        products = products.order_by('product_name')
    elif sort_param == 'price':
        products = products.order_by('price')
    elif sort_param == 'latest':
        products = products.order_by('-publish_date')
    
    return render(request, 'products/manage.html',{
        'products' : products,
        'query' : query,
        'categories' : categories,
        'category_id' : category_id,
        'sort_param' : sort_param,
    })
    
@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    
    return redirect('product:manage')

@login_required
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()
            
            return redirect('product:detail', pk=product.id)
    else:
        form = EditItemForm(instance=product)
    
    return render(request, 'products/form.html',{
        'form': form,
        'title': 'Edit item',
    })