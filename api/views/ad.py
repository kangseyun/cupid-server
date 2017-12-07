import hashlib
from datetime import timedelta, datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from api.models import UserDetail, Ads

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from datetime import datetime
from api.models import Ads, Category, Location, AdTrade, ADResult
from django.shortcuts import redirect


response_data = {}


def trade(request):
    adbos = request.GET.get('id')
    ad = request.GET.get('ad')
    #adobj = Ads.objects.get(id=0)
    ad_obj = Ads.objects.get(id=ad)
    user = UserDetail.objects.get(id=adbos)
    my = UserDetail.objects.get(id=request.user.id)
    try:
        t = AdTrade(creater = user, adbos = user, status=0, ad=ad_obj)
        t.save()
    except:
        print("fail")
    return redirect('my')


def trade_accept(request):
    ad = request.GET.get('ad')
    #adobj = Ads.objects.get(id=0)
    ad_obj = Ads.objects.get(id=ad)

    try:
        obj = AdTrade.objects.get(ad=ad_obj)
        obj.status = 1
        obj.save()
    except:
        print("fail")
    return redirect('my')

@csrf_exempt
def ad_detail(request, id=1):
    if request.method == 'GET':
        check = False
        try:
            obj = Ads.objects.get(id=id)
            t = AdTrade.objects.filter(ad = obj)
            for i in t:
                if i.creater.id == request.user.id:
                    check = True

        except Ads.DoesNotExist:
            pass
        return render(request, 'ad_detail.html', {"view": obj, "num": id, "check": check})


def ad(request):
    if request.method == "GET":
        id = request.GET.get('category', 0)
        category = Category.objects.all()
        print(id)
        if id == 0:
            obj = Ads.objects.all()
        else:
            c = Category.objects.get(id=id)
            print(c)
            obj = Ads.objects.filter(category=c)
            print(obj)
        return render(request, 'ad_list.html', {"ad": obj, "category": category})


def ad_count(request):
    if request.method == "GET":
        count = Ads.objects.count()
        response_data['code'] = 1
        response_data['count'] = count
    else:
        response_data['code'] = -1
    return JsonResponse(response_data, safe=False)


def ad_write(request):
    if request.method == "POST":
        category = request.POST.get('category')
        title = request.POST.get('subject')
        budget = request.POST.get('budget')
        content = request.POST.get('content')
        limit = request.POST.get('limit', 0)
        img = request.FILES['img']
        location_x = request.POST.get('x', 0)
        location_y = request.POST.get('y', 0)
        location_title = request.POST.get('location')
        print(location_x, location_y, location_title)

        # 주소 저장
        if location_x and location_y and location_title:
            location_obj = Location(x = location_x, y = location_y, title = location_title)
            location_obj.save()
        # validation
        if category and title and budget and img:
            ad = Category.objects.get(id=category)
            user = UserDetail.objects.get(user=request.user)

            try:
                obj = Ads(category=ad, title=title, author=user, budget=budget, content=content, limit=limit, img=img, location=location_obj)
                obj.save()
            except:
                obj = Ads(category=ad, title=title, author=user, budget=budget, content=content, limit=limit, img=img)
                obj.save()
            return redirect('my')
        else:
            return redirect('ad_write')
    elif request.method == "GET":
        category = Category.objects.all()
        return render(request, './my/ad_write.html', {'category': category})


@csrf_exempt
def ad_result(request, id=0):
    adtrade = AdTrade.objects.get(id=id)
    try:
        result = ADResult.objects.get(ad=adtrade.ad)
    except:
        return redirect('my')
    if request.method == 'GET':
        return render(request, 'ad_result.html')
