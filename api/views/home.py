from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from api.models import Ads, Category, UserDetail


def index(request):
    ad = Ads.objects.all()
    return render(request, './index.html', {'ad': ad})

def my(request):
    return render(request, './my/index.html', {})


def chat(request):
    return render(request, './my/chat.html', {})

def trade(request):
    return render(request, './my/trade.html', {})

def ad_status(request):
    user = UserDetail.objects.get(user=request.user)
    ad = Ads.objects.filter(author=user)
    return render(request, './my/ad_status.html', {'ad': ad})

def notification(requset):
    return render(requset, './my/notification.html', {})
