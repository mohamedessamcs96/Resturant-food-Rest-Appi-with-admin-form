from django.db import models

# Create your models here.



class Menu(models.Model):
    mealname=models.CharField(max_length=40)
    price=models.IntegerField()
    

    def __str__(self):
        return self.mealname