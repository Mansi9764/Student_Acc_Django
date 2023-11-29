from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50, null=False)
    email=models.EmailField(max_length=100, null=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=100, null=False)

# class Contact(models.Model):
#     contactName=models.CharField(max_length=50, null=False)
#     email=models.EmailField(max_length=100, null=False)
#     notes=models.CharField(max_length=500)
#     createdTime=models.DateTimeField()


    def __str__(self):
        return self.name



