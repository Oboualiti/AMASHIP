from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=300)
    content = models.TextField()
    rating = models.CharField(max_length=100)
    price = models.FloatField()
    url=models.CharField(max_length=300)
    image=models.ImageField(null=True, blank=True ,upload_to='photo/%y/%m/%d')
    image1=models.ImageField(null=True, blank=True ,upload_to='photo/%y/%m/%d')
    image2=models.ImageField(null=True, blank=True, upload_to='photo/%y/%m/%d')
    image3=models.ImageField(null=True, blank=True,upload_to='photo/%y/%m/%d')
    image4=models.ImageField(null=True, blank=True,upload_to='photo/%y/%m/%d')
    image5=models.ImageField(null=True, blank=True,upload_to='photo/%y/%m/%d')

    def __str__(self):
       return self.name    
    

class Email(models.Model):
   email=models.CharField(max_length=50)
   def __str__(self):
      return self.email
         