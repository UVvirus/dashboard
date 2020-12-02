from django.db import models

# Create your models here.
class Employee(models.Model):
    #objects = None
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=50)
    office=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    start_date=models.DateField()
    salary=models.PositiveIntegerField()


    def __str__(self):
        return self.name