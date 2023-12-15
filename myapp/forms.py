from django import forms
from myapp.models import UserProfile 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['bio','profile_picture']
    widgets={
        'bio':forms.Textarea(attrs={'placeholder':'Bio'}),
        'profile_picture':forms.ClearableFileInput(
            attrs={"class":"form-control"}
        )
}