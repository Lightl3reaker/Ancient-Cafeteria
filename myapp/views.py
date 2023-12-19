from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from myapp.models import carousel_img,Product
from .forms import SignupForm,UserProfileForm
from myapp.models import carousel_img,Product,Tag

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
    if request.method=="POST":
        form = SignupForm()
        #if form.is_valid():
         #   form.save()
          #  return redirect('home')
    else:
        form=SignupForm()   
    return render(request,'registration/signup.html',{'form':form})
def profile(request):
    form=UserProfileForm()
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'Account/profile.html',{'form':form})
@login_required
def products_view(request):
    products=Product.objects.all()
    return render(request,"myapp/products.html",
                  {'products':products,'counts':counts,'tags':tags})

class CustomLogin(LoginView):
    template_name="registration/customlogin.html"
class CustomLogout(LogoutView):
    template_name="registration/customlogout.html"
    
#class CustomSignup(CreateView):
#   template_name='registration/signup.html'
#   form_class=SignupForm
#   success_url=reverse_lazy('login')

def Filterby(request,slug=None):
    products=Product.objects.filter(tags__slug=slug)
    return render(request,'myapp/products.html',{
        'products':products,
        'counts':counts,
        'tags':tags,
        })
