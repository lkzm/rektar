from django.shortcuts import render
from cp import models, forms
from django.http import HttpResponseRedirect
import pdb
import datetime
from cp.views.quest import quest_board
from cp.views.room import room
from cp.views.funct import NavMenu


#login view
def login(request, context= {} ):
    request.session['npc']=False
    form = forms.LogInForm(request.POST)
    context['form']=form
    if form.is_valid():
        usr=form.cleaned_data['username']
        pwd=form.cleaned_data['password']
        p=models.Player.objects.get(username=usr, password=pwd)
        request.session['pk_user'] = p.pk
        if (p.npc==True):                #check if the user is a npc
            request.session['npc']=True
            
            return quest_board(request)

        else:
            return room(request)
        ##except: ne pomnq, probably useless
        ###    return render(request, 'cp/login.html', context)

    else:
        return render(request, 'cp/login.html', context)

    return render(request, 'cp/login.html', context)



#registration shte se restruckturira sig 
def create_char(request, context = {}):
    form = forms.CreateCharForm(request.POST)
    context['form']=form
    if form.is_valid():
        usr=form.cleaned_data['username']
        pwd=form.cleaned_data['password']
        try:
            p=models.Player.objects.create(username=usr, password=pwd)
        except:
            return create_char(request)
        char_name=form.cleaned_data['name']
        char_race=form.cleaned_data['race']
        char_cls=form.cleaned_data['cls']
        j=models.Journal.objects.create(player=p)
        d=models.Description.objects.create(text=form.cleaned_data['description'])

        c=models.Character.objects.create(name=char_name,
                cls=char_cls,
                race=char_race,
                player=p,
                description=d)
        request.session['pk_user'] = p.pk
        return room(request)




    else:
        return render(request, 'cp/create_char.html', context)

    return render(request, 'cp/create_char.html', context)
