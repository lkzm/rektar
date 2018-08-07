from django.shortcuts import render
from cp import models, forms

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
import datetime



def quest_board (request, context = {}):
    adventures=models.Adventure.objects.all()
    if (request.session['npc'] == False):
        context['player_adventures']=models.Adventure.objects.filter(characters__pk=request.session['pk_user'])
        context['open_adventures']=models.Adventure.objects.filter(status=1)
        context['selected']="quest_board"
        return render(request, 'cp/player/quest_board.html', context)
    else:
        context['open_adventures']=models.Adventure.objects.filter(status=1)
        context['started_adventures']=models.Adventure.objects.filter(status=0)
        context['finished_adventures']=models.Adventure.objects.filter(status=-1)
        context['selected']="quest_board"
        return render(request, 'cp/npc/quest_board.html', context)




def quest_enroll (request, adventure_id):
    if (request.session['npc']==True):
        return quest_board(request)
    else:

        p=models.Player.objects.get(pk=request.session['pk_user'])
        a=models.Adventure.objects.get(pk=adventure_id)
        j=models.Journal.objects.get(player=p)
        j.adventures.add(a)
        j.save()
        a.characters.add(models.Character.objects.get(player=p))
        a.party_size = a.party_size - 1
        a.save()
        return quest_board (request)


def quest_start (request, adventure_id):
    if (request.session['npc']==True):
        a=models.Adventure.objects.get(pk=adventure_id)
        a.status=0
        a.save()
        return quest_board(request)
    else:
        return quest_board(request)



def quest_finish (request, adventure_id):
    if (request.session['npc']==True):
        a=models.Adventure.objects.get(pk=adventure_id)
        a.status=-1
        a.save()
        return quest_board(request)
    else:
        return quest_board(request)






def quest_create (request):
    if (request.session['npc']==False):
        return quest_board(request)
    else:
        form=forms.QuestForm(request.POST)
        n=models.Player.objects.get(pk=request.session['pk_user'])


        context = {
            'player' : n,
            'form' : form,
            }
        if form.is_valid():
            s=form.cleaned_data['party_size']
            d=form.cleaned_data['description']
            nex=form.cleaned_data['date_next']
            m=form.cleaned_data['name']
            a=models.Adventure.objects.create(
                creator=n,
                name=m,
                date_created=datetime.datetime.today(),
                status=1,
                description=models.Description.objects.create(text=d),
                date_next=nex
                )
            return quest_board(request)
        else:
            return render(request, 'cp/npc/quest_create.html', context)
            return render(request, 'cp/npc/quest_create.html', context)

    return render(request, 'cp/npc/quest_create.html', context)


#/quest%id
def quest_details (request, adventure_id):
    a=models.Adventure.objects.get(pk=adventure_id)
    context = { 'adventure' : a }
    if (request.session['npc']==True):
        return render(request, 'cp/npc/quest_details.html', context)
    else:

        return render(request, 'cp/player/quest_details.html', context)



#add edit quest and remove quest




#edit quest quest_edit%id
#class QuestUpdate (UpdateView):
