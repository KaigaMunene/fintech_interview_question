from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
