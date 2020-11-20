from django.db import models
# Create your models here.
class myData(models.Model):                
        LogoLinks = models.CharField(max_length=122)
        LogoName= models.CharField(max_length=122)


        def __str__(self):
               return self.LogoName
