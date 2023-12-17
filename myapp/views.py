from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
#<<<<<<< HEAD
from myapp.models import carousel_img,Product
from .forms import SignupForm
#=======
from myapp.models import carousel_img,Product,Tag
#>>>>>>> 5dd76a5ea0d86ba7fc7d7455814f2930274e8410

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# Create your views here.
#DB_MOdels
#carousel_img==>fetching carousel images
#Product --> fetching Products
#counts is for showing number of products !!!important

counts=Product.objects.count()
tags=Tag.objects.all()

def index(request):
    if request.user.is_authenticated == True:
        status=True
    else:
        status=False
    carousel_imgs=carousel_img.objects.all()
    return render(request,'myapp/index.html',
                  {'carousel_imgs':carousel_imgs,'counts':counts,'status':status})
    
def signup(request):
    form = SignupForm()
    return render(request,'registration/signup.html')

@login_required
def products_view(request):
    products=Product.objects.all()
    return render(request,"myapp/products.html",
                  {'products':products,'counts':counts,'tags':tags})

class CustomLogin(LoginView):
    template_name="registration/customlogin.html"
class CustomLogout(LogoutView):
    template_name="registration/customlogout.html"
    
class CustomSignup(CreateView):
    template_name='registration/signup.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
#<<<<<<< HEAD
    
#=======

def Filterby(request,slug=None):
    products=Product.objects.filter(tags__slug=slug)
    return render(request,'myapp/products.html',{
        'products':products,
        'counts':counts,
        'tags':tags,
        })
#>>>>>>> 5dd76a5ea0d86ba7fc7d7455814f2930274e8410
