from django.db import models

class Student(models.Model):
    First_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Number_room = models.CharField(max_length=30)
    Facultet = models.CharField(max_length=120)
    Course = models.CharField(max_length=10)

