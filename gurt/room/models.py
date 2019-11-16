from django.db import models
class Room(models.Model):
      Number = models.CharField(max_length=30)
      Name_Student = models.CharField(max_length=30)
      Last_nameStudent = models.CharField(max_length=30)
      slug = models.SlugField(max_length=200, default='')