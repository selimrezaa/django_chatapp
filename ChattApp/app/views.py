from django.shortcuts import render
from .models import *
# Create your views here.

def index(request, groupname):
    group = Group.objects.filter(group_name=groupname).first()
    chat = []
    if group:
        chat = Chat.objects.filter(group=group) 
    else:
        group = Group(group_name=groupname).save()

    context = {
        'groupname': groupname,
        'chat': chat,
    }
    return render(request, 'index.html', context)