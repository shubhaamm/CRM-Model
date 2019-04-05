from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class Meta:
        db_table = "employee"


class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
class Meta:
        db_table = "employees"

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='likes')


class Book(models.Model):
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.pdf

