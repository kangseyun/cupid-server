import hashlib

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


response_data = {
    'status': 'token_ok', 
    'email': '',
    'token': '',
    'code:': 0,
    'data': '',
}


@csrf_exempt
def ad_detail(request, id=0):
    if request.method == 'GET':
        try:
            obj = Ads.objects.filter(id=id)
            response_data['data'] = serializers.serialize('json', obj)
        except Ads.DoesNotExist:
            response_data['code'] = -1
    elif request.method == 'PUT':
        print("Hello")
    elif request.method == 'DELETE':
        print("Hello")
    

    return JsonResponse(response_data, safe=False)


@csrf_exempt
def ad(request):
    if request.method == "GET":
        data = serializers.serialize("json", Ads.objects.all())
        return JsonResponse(data, safe=False)
    if request.method == "POST":
        return JsonResponse(response_data, safe=False)


@csrf_exempt
def ad_write(request):
    if request.method == "POST":
        form = AdsValidation(request.POST, instance)
        if not form.is_valid():
            print("Error")
        else:
            
            ad_type = Ad_type.objects.get(id=form.data['ad_type'])
            obj = Ads(form)
            print("Valied")
    return JsonResponse(response_data, safe=False)
