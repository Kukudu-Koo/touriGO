from django.db import models

# Create your models here.
class newss(models.Model):
    name= models.CharField(max_length=100) 
    img = models.FileField(upload_to='pics')
    desc= models.TextField()