from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Max
from django.db.models import Min
from django.db.models import Q


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
        request.session["userName"] = check["user"].userName
        request.session["user_id"] = check["user"].id
        messages.add_message(request, messages.SUCCESS, "thank you {} for register!".format(request.POST['userName']))
    return redirect("/register1")

def dashboard(request):
    quertyset_list = Product.objects.all()
    print(quertyset_list)
    query = request.GET.get("query")
    if query: 
        quertyset_list = quertyset_list.filter(Q(name__icontains=query) | Q(details__icontains=query) | Q(category__icontains=query)).distinct()

    Products = Product.objects.all()
    Phones = Product.objects.filter(category='Phones')
    Laptops = Product.objects.filter(category='Laptops')
    Television = Product.objects.filter(category='Television')
    Gaming = Product.objects.filter(category='Gaming')

    context = {
        'Products' : quertyset_list,
        'Phones' : Phones,
        'Laptops' : Laptops,
        'Television' : Television,
        'Gaming' : Gaming,

    }

    return render(request, "Price/dashboard.html", context)

def productCategory(request, category):
    productInCategory = Product.objects.filter(category=category)
    # stock = Stock.objects.filter(retaile )
    context = {
        'productInCategory':productInCategory,
        'category':category,
    }

    return render(request, "Price/products.html", context)


def productPage(request, id):
    
    IndividualProduct = Stock.objects.filter(product_id = id)
    # min = Stock.objects.lowestPrice(id)
    # for i in IndividualProduct:
    #     print(i)
    # min = IndividualProduct[0]
    # for i in IndividualProduct:
    #     if IndividualProduct[i] < min:
    #         min = IndividualProduct[i]
    #     return min
    context = {
        "IndividualProduct": IndividualProduct,
        # 'min':min
    }
    return render(request, "Price/productpage.html", context)


def logout(request):
   
      
    return render(request, "Price/logReg.html")
















#def compare(request, id):
# Takes the id of the product clicked or searched.
#Uses that id to get the price of that product from all retailers in the Retailer model
#Compares all the prices and returns the lowest price.
#Display the lowest price.
#Display the highest price.
#Display prices from all retailers as a list on the front-end. 
