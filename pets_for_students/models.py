from django.db import models

# Create your models here.

class Students(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    def __str__(self):
        return self.firstname

class Cats(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
