from django.urls import path

from . import views

app_name = "myapp"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    
]

#