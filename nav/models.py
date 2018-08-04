from django.db import models

# Create your models here.



class MenuOption(models.Model):
    title=models.CharField(max_length=200)
    url=models.CharField(max_length=200)


class Menu(models.Model):
    options=models.ManyToManyField('MenuOption')
    page=models.CharField(max_length=200)
    previous=models.CharField(max_length=200)

