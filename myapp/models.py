from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# Create your models here.
class TestModel(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(default="",blank=True)

class carousel_img(models.Model):
    title=models.CharField(max_length=256)
    idx=models.IntegerField()
    image=models.ImageField(upload_to="carousels/")
    def __str__(self):
        return self.title
        
class Tag(models.Model):
    title=models.CharField(max_length=256,default="",blank=True)
    slug=models.SlugField(blank=True,default='')
    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Tag,self).save()

class Product(models.Model):
    title=models.CharField(max_length=256,default="",blank=True)
    tags=models.ManyToManyField(Tag)
    slug=models.SlugField(blank=True,default='')
    description=models.TextField()
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to='products/')
    image_thumbnail=ImageSpecField(
        source='image',
        processors=[ResizeToFill(350,200)],
        format='JPEG',
        options={'quality':60}
    )
    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Product,self).save()
        
        
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(upload_to='profile_pics/')
    def __str__(self):
        return self.user.username


    