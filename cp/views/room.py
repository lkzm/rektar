from django.shortcuts import render
from cp import models, forms
from django.http import HttpResponseRedirect
import pdb
import datetime
from cp.views.quest import quest_board


#generate room page /room
def room (request):

    try:
        if (request.session['npc'] == True): #npc request player room by id
            player_id=request.session['pk_ph'] #tuka mai nqkakvi exceptions shte trqbvat ama shte go mislim
        else: #players can request only their own rooms
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
    if (request.session['npc'] == True):
        render(request, 'cp/npc/room.html', context)
    else:
        return render(request, 'cp/player/room.html', context)



#request player room as NPC /room%id
def room_request (request, player_id):
    request.session['pk_ph']=player_id
    return room(request)



#future shit: 
#headquaters (dm room)



#nz kakvo sum si mislil ama toku vij sum se setil
def castle (request):
    if (request.session['npc']==False):
        return room(request)
    else:
        return render (request, 'cp/npc/castle.html')



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
    if (request.session['npc']==True):
        return render(request, 'cp/npc/journal.html', context)
    else:
        return render(request, 'cp/player/journal.html', context)


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
    return render(request, 'cp/player/sheets.html', context)

#new element /upload_sheet
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
        return render(request, 'cp/player/upload_sheet.html', context)

    return render(request, 'cp/player/upload_sheet.html', context)


#edit delete for sheets




# /journal/add_note)
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
        return render(request, 'cp/player/add_note.html', context)
    return render(request, 'cp/player/add_note.html', context)
#edit delete for notes 


