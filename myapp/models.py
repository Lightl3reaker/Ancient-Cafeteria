from django.db import models

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

    