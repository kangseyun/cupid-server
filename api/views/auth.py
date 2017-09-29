from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from api.models import UserDetail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import hashlib
from datetime import datetime
import uuid


response_data = {
    'status': 'token_ok', 
    'email': '',
    'token': ''
}

def create_token(email):
    m = hashlib.sha256()
    email = email.join(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    m.update(email.encode('utf-8'))
    return m.hexdigest()


@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        loginInstance = authenticate(username=email, password=password)
        
        if loginInstance is not None:
            token = create_token(loginInstance.email)

            obj = UserDetail.objects.get(user=loginInstance)
            obj.token = token
            obj.save()

            response_data['code'] = 1
            response_data['token'] = token
        else:
            response_data['code'] = 0

    else:
        response_data['code'] = -1
    
    return JsonResponse(response_data, safe=False)


@csrf_exempt
def join(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('userName')
        password = request.POST.get('password')

        if not email or not name or not password:
            response_data['code'] = 2            
        else:
            
            userInstance = User.objects.create_user(name, email, password)
            userInstance.save()

            obj = UserDetail(user = userInstance, user_type=1)
            obj.save()


            response_data['email'] = email
            response_data['code'] = 1
    else:
        response_data['code'] = -1
    return JsonResponse(response_data, safe=False)


@csrf_exempt
def logout(request):
    if request.method == "POST":
        token = request.POST.get('token')

        try:
            userInstance = UserDetail.objects.get(token = token)
            userInstance.token = -1
            userInstance.save()

            response_data['code'] = 1
        except:
            response_data['code'] = -1

    return JsonResponse(response_data, safe=False)


@csrf_exempt
def findEmail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')


        userInstance = UserDetail.objects.filter(email = email)
        if userInstance:
            print("find")
        else:
            print("Not find")
    
    
    return JsonResponse(response_data, safe=False)
