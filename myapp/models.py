from django.db import models

class Resume(models.Model):

    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    rating=models.IntegerField()
    comments=models.TextField()
