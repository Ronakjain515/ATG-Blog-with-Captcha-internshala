from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)

class Blog(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    visibility = models.CharField(max_length=10, choices=[("public", "public"), ("private", "private")])
    image = models.FileField(upload_to="blog/")