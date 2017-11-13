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
from api.models import Ads, Ad_type
from api.validation.AdValidation import AdsValidation


response_data = {}


@csrf_exempt
def ad_detail(request, id=0):
    if request.method == 'GET':
        try:
            obj = Ads.objects.filter(id=id)
            response_data['data'] = serializers.serialize('json', obj)
        except Ads.DoesNotExist:
            response_data['code'] = -1
    elif request.method == 'PUT':
        print("PUT") # 수정
    elif request.method == 'DELETE':
        try:
            instance = Ads.objects.get(id=id)
            instance.delete()
            response_data['code'] = 1
        except:
            response_data['code'] = -1

    return JsonResponse(response_data, safe=False)


@csrf_exempt
def ad(request):
    if request.method == "GET":
        # data = serializers.serialize("json", Ads.objects.all())
        # return JsonResponse(data, safe=False)
        return render(request, 'ad_list.html', {})


@csrf_exempt
def ad_count(request):
    if request.method == "GET":
        count = Ads.objects.count()
        response_data['code'] = 1
        response_data['count'] = count
    else:
        response_data['code'] = -1
    return JsonResponse(response_data, safe=False)


@csrf_exempt
def ad_write(request):
    if request.method == "POST":
        token = request.POST.get('token')
        ad_type = request.POST.get('adType')
        title = request.POST.get('title')
        budget = request.POST.get('budget')
        limit = request.POST.get('limit')

        # validation
        if token and ad_type and title and budget and limit:
            ad = Ad_type.objects.get(id=ad_type)
            user = UserDetail.objects.get(token=token)

            obj = Ads(ad_type=ad, title=title, author=user, budget=budget, limit=limit)
            obj.save()
            response_data['code'] = 1
        else:
            response_data['code'] = -1

    return JsonResponse(response_data, safe=False)
