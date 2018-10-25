from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "Price/logReg.html")
def register(request):
    return render(request, "Price/Register.html")
def dashboard(request):
    
    return render(request, "Price/dashboard.html")
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
    return render(request, "Price/productpage.html")
















#def compare(request, id):
# Takes the id of the product clicked or searched.
#Uses that id to get the price of that product from all retailers in the Retailer model
#Compares all the prices and returns the lowest price.
#Display the lowest price.
#Display the highest price.
#Display prices from all retailers as a list on the front-end. 
