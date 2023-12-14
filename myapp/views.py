from django.shortcuts import render
from myapp.models import carousel_img

# Create your views here.
def index(request):
    carousel_imgs=carousel_img.objects.all()
    return render(request,'myapp/index.html',{'carousel_imgs':carousel_imgs})