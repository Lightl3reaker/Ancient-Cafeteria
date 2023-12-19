from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import UserProfile 

class UserProfileForm(forms.ModelForm):
    bio=forms.CharField( max_length=500, required=False)
    class Meta:
        model=UserProfile
        fields=['bio','profile_picture']
    widgets={
        'bio':forms.Textarea(attrs={'placeholder':'Bio'}),
        'profile_picture':forms.ClearableFileInput(
            attrs={"class":"form-control"}
        )
}
     
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Your username", }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"placeholder": "Your email address",}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Your password", }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm password", }))