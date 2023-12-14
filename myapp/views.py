from django.shortcuts import render
from myapp.models import carousel_img,Product

# Create your views here.
#DB_MOdels
#carousel_img==>fetching carousel images
#Product --> fetching Products
#counts is for showing number of products !!!important
def index(request):
    counts=Product.objects.count()
    carousel_imgs=carousel_img.objects.all()
    return render(request,'myapp/index.html',{'carousel_imgs':carousel_imgs,'counts':counts})
def products_view(request):
    counts=Product.objects.count()
    products=Product.objects.all()
    return render(request,"myapp/products.html",{'products':products,'counts':counts})