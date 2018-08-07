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
            request.session['char']=models.Character.objects.get(player=p).pk
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



def castle (request):
    form = forms.LogInForm(request.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        usr = form.cleaned_data['username']
        pwd = form.cleaned_data['password']
        p = models.Player.objects.get(username=usr, password=pwd)
        request.session['pk_user'] = p.pk
        if (p.npc == True):  # check if the user is a npc
            request.session['npc'] = True

            return quest_board(request)

        else:
            return room(request)
        ##except: ne pomnq, probably useless
        ###    return render(request, 'cp/login.html', context)

    else:
        return render(request, 'cp/index.html', context)

    return render(request, 'cp/index.html', context)

def chamber (request, chamber_id):
    context = {
        'chamber': models.Chamber.objects.get(pk=chamber_id)
    }
    return render(request, 'cp/chamber.html', context)

def edit_chamber (request, chamber_id, context={}):
    ch = models.Chamber.objects.get(pk=chamber_id)
    context['chamber'] = ch
    context['descriptions'] = []

    #if (request.session['npc']==True):

    for description in ch.descriptions.all():
        try:

            if (int(context['edit_id']) == description.id):
                if request.method == 'POST':
                    form = forms.DescriptionForm(request.POST)
                    if form.is_valid():
                        text=form.cleaned_data['text']
                        description.text=text
                        description.save()

                        return edit_chamber(request, chamber_id)
                    else:
                        return edit_chamber(request, chamber_id, context)
                else:

                    form = forms.DescriptionForm(instance=description)
                    context['edit_form'] = form
            else:

                context['descriptions'].append(description)
        except:
            context['descriptions'].append(description)
    if request.method == 'POST':
        new_form = forms.DescriptionForm(request.POST)
        context['new_form'] = new_form
        if new_form.is_valid():
            text=new_form.cleaned_data['text']
            d=models.Description.objects.create()
            d.text=text
            d.save()
            return edit_chamber(request, chamber_id)
        else:
            return render(request, 'cp/npc/edit_chamber.html', context)
    else:
        new_form = forms.DescriptionForm()
        context['new_form'] = new_form
    return render(request, 'cp/npc/edit_chamber.html', context)
    #else:
        #return chamber(request, chamber_id)


def chamber_description_edit (request, chamber_id, description_id):
    context={
        'edit_id': description_id
    }
    return edit_chamber(request, chamber_id, context)

# def chamber_edit (request, chamber_id):
#     ch=models.Chamber.objects.get(pk=chamber_id)
#     forms= []
#     try:
#         for description in ch.descriptions.all():
#             forms.append(forms.DescriptionForm(request.POST))
#         add_form = forms.DescriptionForm(request.POST)
#     except:
#          add_form=forms.DescriptionForm(request.POST)
#
#     context = {
#         'descriptions': models.Chamber.objects.get(pk=chamber_id),
#         'forms' : forms,
#         'add_form' : add_form
#     }
#     return render(request, 'cp/npc/chamber_edit.html', context)
#
# def chamber_create (request):
#     form=forms.ChamberForm(request.POST)
#     ch=models.Chamber.objects.create()
#
#     context = {
#
#         'forms': forms,
#         'add_form': add_form
#     }
#     return render()
#


