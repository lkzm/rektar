from django.db import models
import datetime
 
# Create your models here.

class Player (models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    npc=models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Description(models.Model):
    text=models.CharField(max_length = 40000)
    def __str__(self):
        return self.text



class Character(models.Model):
    player=models.ForeignKey('Player', on_delete=models.CASCADE, default=1) 
    alive=models.BooleanField(default=True)
    name=models.CharField(max_length=100)
    cls=models.CharField(max_length=30)
    race=models.CharField(max_length=30)
    description=models.ForeignKey('Description', on_delete=models.SET_DEFAULT, default=0)

    def __str__(self):
        return self.name + ', '+ self.cls +', ', self.race


class Sheet(models.Model):
    level=models.IntegerField()
    url=models.CharField(max_length=255)
    character=models.ForeignKey('Character', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return str(self.character)

class Memento(models.Model):

    character=models.ForeignKey('Character', on_delete=models.CASCADE)
    description=models.ForeignKey('Description', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.character)

class Note(models.Model):
    date_created=models.DateField(default=datetime.datetime.today())
    description=models.ForeignKey('Description', on_delete=models.CASCADE)
    character=models.ForeignKey('Character', on_delete=models.CASCADE)
    def __str__ (self):
        return str(self.character) + ' on ' + str(self.date_created)

class Adventure(models.Model):
    date_finished=models.DateField(default=datetime.datetime.today)
    date_next=models.DateField(default=datetime.datetime.today)
    date_started=models.DateField(default=datetime.datetime.today)
    date_created=models.DateField(default=datetime.datetime.today)
    status=models.IntegerField(default=False)
    name=models.CharField(max_length=50, default = 'Quest')
    party_size=models.IntegerField(default=5)
    description=models.ForeignKey('Description', on_delete=models.CASCADE)
    characters=models.ManyToManyField('Character')
    notes=models.ManyToManyField('Note')
    creator=models.ForeignKey('Player', on_delete=models.SET_DEFAULT, default = 0 )
    def __str__(self):
        return str(self.name) + ' for ' + self.party_size




class Journal(models.Model):

    player=models.ForeignKey('Player', on_delete=models.CASCADE)
    adventures=models.ManyToManyField('Adventure')
    notes=models.ManyToManyField('Note')











