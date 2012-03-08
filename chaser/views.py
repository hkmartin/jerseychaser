from django.shortcuts import render_to_response




from django.http import HttpResponseRedirect
from django.contrib.messages.api import get_messages


from jersey.chaser.models import Chaser


def homepage(request):
    greeting = "Hi there!"
    chaser = Chaser.objects.all()
    return render_to_response('homepage.html',{ 
        'chaser' : chaser,
        'greeting': greeting,
    })
