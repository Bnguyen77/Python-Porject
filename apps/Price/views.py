<<<<<<< HEAD
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
=======
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
from .models import User, Product
from datetime import datetime

def index(request):
    print('index')
    return render(request, "Price/logReg.html")

def flash_errors(errors, request):
    print(errors)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        
def show_registration_page(request):
    return render(request, "Price/Register.html")
    
def register(request):
    errors = User.objects.validate_registration(request.POST)
    print('register works')
    context = {} 
    if errors: 
        flash_errors(errors, request)

    elif not errors:
        request.session['first_name'] = request.POST['first_name']
        print("first name " + request.session['first_name'])
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        request.session['password_confirmation'] = request.POST['password_confirmation']
        
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        context = {'user' : user}
        print('user created...', user)
        request.session['id'] = user.id 
        return render (request, 'Price/dashboard.html', context)
    return redirect('/register')

def login(request):
    # print('email', request.POST['email'])
    errors = User.objects.validate_login(request.POST)
    if errors: 
        flash_errors(errors, request)
        return render(request, "Price/logReg.html")
    else:
        user = User.objects.get(email = request.POST['email'])
        login_password = request.POST['password']
        request.POST['email'] == user.email
        context = {'user' : user}
        request.session['id'] = user.id 
        print('successful login')
        return render (request, 'Price/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def show_login(request):
    return redirect('/index')

def dashboard(request):
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

def productCategory(request, category):
    productInCategory = Product.objects.filter(category=category)
    context = {
        'productInCategory':productInCategory,
    }

    return render(request, "Price/products.html", context)

def productPage(request, productId):
    IndividualProduct = Stock.objects.filter(product_id=productId)
    context = {
        "IndividualProduct": IndividualProduct
    }
    return render(request, "Price/productpage.html", context)
















#def compare(request, id):
# Takes the id of the product clicked or searched.
#Uses that id to get the price of that product from all retailers in the Retailer model
#Compares all the prices and returns the lowest price.
#Display the lowest price.
#Display the highest price.
#Display prices from all retailers as a list on the front-end. 
>>>>>>> 403cd1e23dd417b909f91f5af2730cce5fe7ba54
