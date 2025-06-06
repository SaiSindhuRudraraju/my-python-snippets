from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .Forms import ProductForm

# Create your views here.
def home(request):
    return HttpResponse("Welcome to myproject1!!")

def hello(request):
    productList = Product.objects.all()
    product_form = ProductForm()
    return render(request, 'hello.html', {'message': 'Hello, world!', 'product_form':product_form, 'productList': productList})

def SaveProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Saved Successfully!!")
        else:
            return HttpResponse("Error saving product.")
    else:
        return HttpResponse("Invalid request method.")