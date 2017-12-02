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
from api.models import Ads, Category, Location
from django.shortcuts import redirect


response_data = {}


@csrf_exempt
def ad_detail(request, id=0):
    if request.method == 'GET':
        try:
            obj = Ads.objects.get(id=id)
        except Ads.DoesNotExist:
            response_data['code'] = -1
        return render(request, 'ad_detail.html', {"view": obj})


# 테스트 위한 render 함수 -> 테스트 후 삭제할 것 !
@csrf_exempt
def ad_detail_render(request, id=0):
    if request.method == 'GET':
        return render(request, 'ad_detail.html')


@csrf_exempt
def ad(request):
    if request.method == "GET":
        obj = Ads.objects.all()
        return render(request, 'ad_list.html', {"ad": obj})


@csrf_exempt
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
                obj = Ads(category=ad, title=title, author=user, budget=budget, limit=limit, img=img, location=location_obj)
                obj.save()
            except:
                obj = Ads(category=ad, title=title, author=user, budget=budget, limit=limit, img=img)
                obj.save()
            return redirect('my')
        else:
            return redirect('ad_write')
    elif request.method == "GET":
        category = Category.objects.all()
        return render(request, './my/ad_write.html', {'category': category})
