from django.shortcuts import render

# Create your views here.
def product_list(request, category_slug=None):
    category = none
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, category_slug)
        products = Product.objects.filter(available=True)
    return render(request, 'store/product/list.html',
                   {'category':category, 'categories':categories, 
                   'products':products})
    
def product_detail(request, id_, slug):
    product = get_object_or_404(Product, id=id_, slug=slug, available=true)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product/detail.html',
                   {'product':product, 'cart_product_form':cart_product_form})
