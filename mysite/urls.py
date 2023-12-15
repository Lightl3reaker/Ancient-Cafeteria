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
from django.urls import path
from myapp import views as myapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp_views.index,name='home'),
    path('products/',myapp_views.products_view,name="products_view"),
    path('accounts/login/',myapp_views.CustomLogin.as_view(),name="login"),
    path('accounts/logout/',myapp_views.CustomLogout.as_view(),name="logout"),
    path('accounts/signup/',myapp_views.CustomSignup.as_view(),name="signup")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
