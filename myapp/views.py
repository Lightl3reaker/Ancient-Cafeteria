from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from myapp.models import carousel_img,Product
from .forms import UserProfileForm
from myapp.models import carousel_img,Product,Tag,UserProfile
from myapp.models import carousel_img,Product,Tag,Contact
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse


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
    user_form=UserCreationForm()
    profile_form=UserProfileForm()
    if request.method=="POST":
        user_form=UserCreationForm(request.POST)
        profile_form=UserProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect('login') 
    return render(request,'registration/signup.html',{'user_form':user_form,'profile_form':profile_form})

@login_required
def view_profile(request):
    try:
        user_profile=UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile=None
    return render(request,'Account/profile_display.html',
                  {
                      'user_profile':user_profile
                  })
@login_required
def edit_profile(request):
    if request.method=='POST':
        form=UserProfileForm(
            request.POST,
            request.FILES,instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=UserProfileForm(instance=request.user.userprofile)
    return render(request,'Account/profile_edit.html',{'form':form})

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

def contact_us(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("<h1>Thanks for contact us..</h1>")
    return render(request ,'myapp/contact.html')    