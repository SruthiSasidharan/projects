from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name=models.CharField(max_length=120)

    def __str__(self):
        return self.brand_name

class Mobiles(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    specs=models.CharField(max_length=200)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.IntegerField()
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.mobile_name
