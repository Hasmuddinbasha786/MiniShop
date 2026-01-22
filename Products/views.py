
from django.shortcuts import render,redirect
from Products.models import *
from django.core.paginator import Paginator
from django.contrib import messages


def base(request):
    return render(request,'base.html')




def category_list(request):
    category_qs = Category.objects.all().order_by('-id')

    search_query = request.GET.get('q', '')
    per_page = request.GET.get('per_page', 5) #default 5


    if search_query:
        category_qs = category_qs.filter(name__icontains = search_query)
    total_count = category_qs.count()

    if per_page == 'all':
        categories =category_qs

    else:
        paginator = Paginator(category_qs, int(per_page))
        page_number = request.GET.get('page') 
        categories = paginator.get_page(page_number)
    

    return render(request,'category/category_list.html',{
        'categories': categories,  #paginated data
        'total_count': total_count, #total records
        'per_page' : per_page,
        'search_query' : search_query,
    })


def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Category.objects.filter(name=name).exists():
            messages.error(request, "Category already exists")
            return redirect('categoryadd')

        if name:
            Category.objects.create(name = name)
            messages.success(request,'Category Created Successfully')
            return redirect('categorylist')
        
    return render(request, 'category/category_add.html')


def category_edit(request, id):

    category = Category.objects.filter(id = id).first()

    if not category:
        return redirect('categorylist')

    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            category.name = new_name
            category.save()

        return redirect('categorylist')
    
    return render(request,'category/category_edit.html',{
        'category' : category
    })


def category_delete(request, id):
    category = Category.objects.filter(id = id)

    if category.exists():
        category.delete()
        messages.success(request,'Category Deleted Successfully.')

    else:
        messages.error(request,'Category Not Found.')
    return redirect('categorylist')










# Brand

def brand_list(request):
    brand_qs = Brand.objects.all().order_by('-id')

    search_query = request.GET.get('q', '')
    per_page = request.GET.get('per_page', 5) #default 5


    if search_query:
        brand_qs = brand_qs.filter(name__icontains = search_query)
    total_count = brand_qs.count()

    if per_page == 'all':
        brands =brand_qs

    else:
        paginator = Paginator(brand_qs, int(per_page))
        page_number = request.GET.get('page') 
        brands = paginator.get_page(page_number)
    

    return render(request,'brand/brand_list.html',{
        'brands': brands,  #paginated data
        'total_count': total_count, #total records
        'per_page' : per_page,
        'search_query' : search_query,
    })


def brand_add(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')

        if Brand.objects.filter(name=name).exists():
            messages.error(request, "brand already exists")
            return redirect('brandadd')

        if name and category_id:
            category = Category.objects.get(id=category_id)
            Brand.objects.create(name = name, category = category)
            messages.success(request,'brand Created Successfully')
            return redirect('brandlist')
        
    return render(request, 'brand/brand_add.html',{
        'categories' : categories,
    })














def brand_edit(request, id):

    brand = Brand.objects.filter(id = id).first()
    categories = Category.objects.all()

    if not brand:
        messages.error(request,'Brand not found.')
        return redirect('brandlist')

    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_category_id = request.POST.get('category')

        if new_name and new_category_id:
            # Check duplicate
            if Brand.objects.filter(name=new_name,category_id = new_category_id).exclude(id=id).exists():
                messages.error(request, "Brand already exists in this category.")
                return redirect('brandedit', id=id)
            
            brand.name = new_name  # update instance
            brand.category_id = new_category_id
            brand.save()           # save changes
            messages.success(request, "Brand updated successfully")
        return redirect('brandlist')
    
    return render(request,'brand/brand_edit.html',{
        'brand' : brand,
        'categories' : categories,
    })


def brand_delete(request, id):
    brand = Brand.objects.filter(id = id)

    if brand.exists():
        brand.delete()
        messages.success(request,'Brand Deleted Successfully.')

    else:
        messages.error(request,'Brand Not Found.')
    return redirect('brandlist')



















def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    brands = Brand.objects.all()

    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')

    if category_id:
        products = products.filter(category_id = category_id)

    if brand_id:
        products = products.filter(brand_id = brand_id)

    return render(request, 'products/product_list.html',{
        'products': products,
        'brands' : brands,
        'categories' :categories,
    })



def product_add(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')
        brand_id = request.POST.get('brand')

        Product.objects.create(
            name = name,
            price = price,
            description = description,
            stock = stock,
            category_id = category_id,
            brand_id = brand_id
        )

        return redirect('product_list')
    
    return render(request, 'products/product_add.html',{
        'categories' : categories,
        'brands' : brands,
    })

