from django.shortcuts import render
from myapp.models import carousel_img,Product

# Create your views here.
def index(request):
    carousel_imgs=carousel_img.objects.all()
    return render(request,'myapp/index.html',{'carousel_imgs':carousel_imgs})
def products_view(request):
    products=Product.objects.all()
    return render(request,"myapp/products.html",{'products':products})