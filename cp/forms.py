from django import forms
from cp import models

class CreateCharForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=50)
    name=forms.CharField(max_length=100)
    cls=forms.CharField(max_length=30)
    race=forms.CharField(max_length=30)
    description=forms.CharField(widget=forms.Textarea)
class LogInForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=50)
class UploadSheet(forms.Form):
    url=forms.CharField(max_length=255)
    level=forms.IntegerField()
class NoteForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)
class QuestForm(forms.Form):
    name=forms.CharField(max_length=50)
    description=forms.CharField(widget=forms.Textarea)
    party_size=forms.IntegerField()
    date_next=forms.DateField()




class DescriptionForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)

class ChamberForm(forms.Form):
    text=forms.CharField(max_length=200)



