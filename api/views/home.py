from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, './index.html', {})


def my(request):
    return render(request, './my/index.html', {})


def chat(requset):
    return render(requset, './my/chat.html', {})


def notification(requset):
    return render(requset, './my/notification.html', {})

def ad_write(requset):
    return render(requset, './my/ad_write.html', {})