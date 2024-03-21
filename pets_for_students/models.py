from django.db import models

# Create your models here.

class Students(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    noOfCats = models.IntegerField(default=0)
    def __str__(self):
        return self.firstname

class Cats(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.student.noOfCats = self.student.cats_set.count() + 1
        self.student.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
