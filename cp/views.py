from django.shortcuts import render
from cp import models, forms
from django.http import HttpResponseRedirect
import pdb
import datetime
from cp.quest import quest_board



#room view /room 
def room (request):

    try:
        if (request.session['npc'] == True):
            player_id=request.session['pk_ph']
        else:
            player_id=request.session['pk_user']
    except:
        return login(request)
    p=models.Player.objects.get(pk=player_id)
    c=models.Character.objects.get(player=player_id)
    m=models.Memento.objects.filter(character=c.pk)
    j=models.Journal.objects.get(player=p)
    
    context = {
            'player' : p,
            'character': c,
            'mementos': m,
            'journal': j,
            'selected': "room",
            }
    return render(request, 'cp/room.html', context)



#request player room as NPC
def room_request (request, player_id):
    request.session['pk_ph']=player_id
    return room(request)


#i am not using that yet
def castle (request):
    if (request.session['npc']==False):
        return room(request)
    else:
        return render (request, 'cp/npc/castle.html')



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
        ##except:
        ###    return render(request, 'cp/login.html', context)

    else:
        return render(request, 'cp/login.html', context)

    return render(request, 'cp/login.html', context)



#registration
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




#sheets view /sheets
def sheets (request):
    if (request.session['npc']==True):
        p=models.Player.objects.get(pk=request.session['pk_ph'])
    else:
        p=models.Player.objects.get(pk=request.session['pk_user'])
    c=models.Character.objects.get(player=p)
    s=models.Sheet.objects.filter(character=c)
    context = {
            'sheets' : s,
            'character' : c,
            'selected2' : "sheets",
            'selected' : "room",
            }
    return render(request, 'cp/sheets.html', context)



#upload sheet /upload_sheet
def upload_sheet (request):
    if (request.session['npc']==True):
        p=models.Player.objects.get(pk=request.session['pk_ph'])
    else:    
        p=models.Player.objects.get(pk=request.session['pk_user'])
    c=models.Character.objects.get(player=p)
    form = forms.UploadSheet(request.POST)
    context = {
            'character' : c,
            'form' : form,
            'selected': "room",
            'selected2': "sheets",
            }
    if form.is_valid():
        u=form.cleaned_data['url']
        l=form.cleaned_data['level']
        s=models.Sheet.objects.create(
                url=u,
                level=l,
                character=c)
        return sheets(request)




    else:
        return render(request, 'cp/upload_sheet.html', context)

    return render(request, 'cp/upload_sheet.html', context)



#journal /journal
def journal (request):
    if (request.session['npc']==True):
        player_id=request.session['pk_ph']

    else:    
        player_id=request.session['pk_user']
    p=models.Player.objects.get(pk=player_id)
    c=models.Character.objects.get(player=p)
    j=models.Journal.objects.get(player=p)
    context = {
            'player' : p,
            'notes' : j.notes,
            'character' : c,
            'adventures' : j.adventures,
            'journal' : j,
            'selected' : "room",
            'selected2' : "journal",
            }
    return render(request, 'cp/journal.html', context)
def add_note (request):
    if (request.session['npc']==True):
        p=models.Player.objects.get(pk=request.session['pk_ph'])
    else:    
        p=models.Player.objects.get(pk=request.session['pk_user'])
    c=models.Character.objects.get(player=p)
    form = forms.NoteForm(request.POST)
    j=models.Journal.objects.get(player=p)
    context = {
            'character' : c,
            'form' : form,
            'selected' : "room",
            'selected2' : "journal",
            }
    if form.is_valid():
        text=form.cleaned_data['text']
        d=models.Description.objects.create(text=text)
        n=models.Note.objects.create(character=c,
                description=d,
                date_created=datetime.datetime.now())
        j.notes.add(n)
        return journal(request)
    else:
        return render(request, 'cp/add_note.html', context)
    return render(request, 'cp/add_note.html', context)



