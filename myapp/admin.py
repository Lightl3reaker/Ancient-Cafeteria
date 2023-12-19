from django.contrib import admin
from myapp.models import TestModel,carousel_img,Tag,Product,Contact
# Register your models here.
admin.site.register(TestModel)
admin.site.register(carousel_img)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Contact)

