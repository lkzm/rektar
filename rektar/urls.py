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
from cp import views, quest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('room/', views.room, name='room'),
    path('create_char/', views.create_char, name='create_char'),
    path('sheets/', views.sheets, name='sheets'),
    path('upload_sheet/', views.upload_sheet, name='upload_sheet'),
    path('journal/', views.journal, name='journal'),
    path('add_note/', views.add_note, name="add_note"),
    path('quest_board/', quest.quest_board, name='quest_board'),
    path('quest_enroll%<int:adventure_id>/', quest.quest_enroll, name='quest_enroll'),
    path('quest_start%<int:adventure_id>/', quest.quest_start, name='quest_start'),
    path('quest_finish%<int:adventure_id>/', quest.quest_finish, name='quest_start'),
    path('quest_create/', quest.quest_create, name='quest_create'),
    path('castle/', views.castle, name='castle'),
    path('room_request%<int:player_id>/', views.room_request, name='room_request'),
    path('quest_details%<int:adventure_id>', quest.quest_details, name='quest_details'),
    #path('create_npc/', views.room_create, name='create_npc'),
]

