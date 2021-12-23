from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Service(models.Model):
    price=models.IntegerField()
    category=models.CharField( max_length=100)
    img=models.ImageField()
    description=models.TextField(default='cwv')
    def __str__(self):
        return self.category
class Staff(models.Model):
    full_name=models.CharField(max_length=200)
    position=models.CharField(max_length=100)
    img=models.ImageField()
class Person(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=12)
    def __str__(self) :
        return self.name+" "+self.phone

class Record(models.Model):
    time=models.TimeField()
    service=ForeignKey(Service,on_delete=CASCADE)
    customer=ForeignKey(Person,on_delete=CASCADE,blank=True)

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def str(self):
        return self.name
