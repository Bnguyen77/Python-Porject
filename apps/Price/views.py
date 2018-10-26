from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "Price/logReg.html")
def register1(request):
    return render(request, "Price/register.html")

def register(request):
    check = User.objects.register(
        request.POST['userName'],
        request.POST['email'],
        request.POST['password'],
        request.POST['password2'],
    )
    if not check["valid"]:
        for error in check["errors"]:
            messages.add_message(request, messages.ERROR, error)
    else:
        request.session["user_id"] = check["user"].id
        messages.add_message(request, messages.SUCCESS, "thank you {} for register!".format(request.POST['userName']))
    return redirect("/register1")

def dashboard(request):
    quertyset_list = Product.objects.all()
    print(quertyset_list)
    query = request.GET.get("query")
    if query: 
        quertyset_list = quertyset_list.filter(name__icontains=query).distinct()
    
    Products = Product.objects.all()
    Phones = Product.objects.filter(category='Phones')
    Laptops = Product.objects.filter(category='Laptops')
    Television = Product.objects.filter(category='Television')
    Gaming = Product.objects.filter(category='Gaming')

    context = {
        'Products' : Products,
        'Phones' : Phones,
        'Laptops' : Laptops,
        'Television' : Television,
        'Gaming' : Gaming,

    }

    return render(request, "Price/dashboard.html", context)

def show_product_detail(request, id):
    product = Product.objects.get(id = id)
    print(product.name)
    context = {
        'product' : product
    }
    return render(request, 'Price/productdetail.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')


# def productCategory(request, category):
#     productInCategory = Product.objects.filter(category=category)
#     context = {
#         'productInCategory':productInCategory,
#     }

#     return render(request, "Price/products.html", context)
# def productPage(request, productId):
#     IndividualProduct = Stock.objects.filter(product_id=productId)
#     context = {
#         "IndividualProduct": IndividualProduct
#     }
#     return render(request, "Price/productpage.html", context)
















#def compare(request, id):
# Takes the id of the product clicked or searched.
#Uses that id to get the price of that product from all retailers in the Retailer model
#Compares all the prices and returns the lowest price.
#Display the lowest price.
#Display the highest price.
#Display prices from all retailers as a list on the front-end. 
