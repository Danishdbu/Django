from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)
    rollNo = models.IntegerField()
    # def __str__(self):
    #     return self.name

class Result(models.Model):
    stud_class = models.CharField(max_length=70)
    marks = models.IntegerField()
    # def __str__(self):
    #     return str(self.stud_class)