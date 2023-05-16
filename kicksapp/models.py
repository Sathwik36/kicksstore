from django.db import models

# Create your models here.
class data(models.Model):
    username=models.CharField(max_length=50)
    passs=models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
class feedback1(models.Model):
    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=10)
    email=models.CharField( max_length=50)
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class mailm(models.Model):
    email=models.EmailField(max_length=54)
    otp=models.IntegerField()
    addr=models.TextField()

    def __str__(self) :
        return self.email
    