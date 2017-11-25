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
from api.models import Ads, Category
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


def ad_write(request):
    if request.method == "POST":
        category = request.POST.get('category')
        title = request.POST.get('subject')
        budget = request.POST.get('budget')
        limit = request.POST.get('limit', 0)
        # validation
        if category and title and budget:
            ad = Category.objects.get(id=category)
            user = UserDetail.objects.get(user=request.user)

            obj = Ads(category=ad, title=title, author=user, budget=budget, limit=limit)
            obj.save()
            return redirect('my')
        else:
            return redirect('ad_write')
    elif request.method == "GET":
        category = Category.objects.all()
        return render(request, './my/ad_write.html', {'category': category})
