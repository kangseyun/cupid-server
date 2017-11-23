from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from api.models import Ads, Category, UserDetail


def index(request):
    ad = Ads.objects.all()
    return render(request, './index.html', {'ad': ad})

def my(request):
    return render(request, './my/index.html', {})


def chat(requset):
    return render(requset, './my/chat.html', {})


def notification(requset):
    return render(requset, './my/notification.html', {})
