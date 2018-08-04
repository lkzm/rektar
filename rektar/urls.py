"""rektar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from cp.views import quest, account, room

urlpatterns = [
    path('admin/', admin.site.urls),

    #views/accounts.py
    path('login/', account.login, name='login'),
    path('create_char/', account.create_char, name='create_char'),
    #path('create_npc/', views.room_create, name='create_npc'),
        
    #views/room.py
    path('room/', room.room, name='Room'),
    path('sheets/', room.sheets, name='Sheets'),
    path('upload_sheet/', room.upload_sheet, name='Upload Sheet'),
    path('journal/', room.journal, name='Journal'),
    path('journal/add_note/', room.add_note, name="Journal Note"),
    path('room%<int:player_id>/', room.room_request, name='Room'),
    #path('castle/', views.castle, name='castle'),
        
    #views/quest.py
    path('quest_board/', quest.quest_board, name='quest_board'),
    path('quest_enroll%<int:adventure_id>/', quest.quest_enroll, name='quest_enroll'),
    path('quest_start%<int:adventure_id>/', quest.quest_start, name='quest_start'),
    path('quest_finish%<int:adventure_id>/', quest.quest_finish, name='quest_start'),
    path('quest%<int:adventure_id>', quest.quest_details, name='quest_details'),
    path('quest_create/', quest.quest_create, name='quest_create'),
    #path('quest/add_note/', quest.add_note, name="journal_note"),
]

