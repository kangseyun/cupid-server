from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from api.models import Ads, Category, UserDetail, Notification, AdTrade


# def index(request):
#     ad = UserDetail.objects.all()
#     return render(request, './index.html', {'ad': ad})


def my(request):
    user = UserDetail.objects.get(user=request.user)
    return render(request, './my/index.html', {"user": user})

def chat(request):
    return render(request, './my/chat.html', {})

def trade(request):
    user = UserDetail.objects.get(user = request.user)
    obj = AdTrade.objects.filter(adbos=user)
    for i in obj:
        print(i)
    return render(request, './my/trade.html', {'ad': obj})

def ad_result(request):
    user = UserDetail.objects.get(user=request.user)
    obj = AdTrade.objects.filter(status=1, adbos=user)
    return render(request, './my/ad_result.html', {'ad': obj})

def ad_status(request):
    user = UserDetail.objects.get(user=request.user)
    ad = Ads.objects.filter(author=user)
    return render(request, './my/ad_status.html', {'ad': ad})

def notification(request):
    user = UserDetail.objects.get(user=request.user)
    noti = Notification.objects.filter(user=user)
    return render(request, './my/notification.html', {'noti': noti})
