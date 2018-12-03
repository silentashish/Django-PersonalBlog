from django.db import models

# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=256)
    length=models.PositiveIntegerField()
    releaseYear=models.PositiveIntegerField()

    def __str__(self):
        return self.title

class customer(models.Model):
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    phone=models.PositiveIntegerField()

    def __str__(self):
        return self.first_name+' '+self.last_name
