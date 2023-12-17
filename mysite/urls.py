"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views as myapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('',myapp_views.index,name='home'),
    path('products/',myapp_views.products_view,name="products_view"),
    path('filterby/<slug:slug>/',myapp_views.Filterby,name="products_filter"),
    path('accounts/login/',myapp_views.CustomLogin.as_view(),name="login"),
    path('accounts/logout/',myapp_views.CustomLogout.as_view(),name="logout"),
<<<<<<< HEAD
    path('accounts/signup/',myapp_views.CustomSignup.as_view(),name="signup")

=======
    path('accounts/signup/',myapp_views.CustomSignup.as_view(),name="signup"),
>>>>>>> 5dd76a5ea0d86ba7fc7d7455814f2930274e8410
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
