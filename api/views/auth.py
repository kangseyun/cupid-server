from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from api.models import UserDetail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import hashlib
from datetime import datetime


response_data = {
    'status': 'token_ok', 
    'email': '',
    'token': ''
}

def create_token(email):
    m = hashlib.sha256()
    m.update(email+datetime.now())
    return m.hexdigest()


@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        loginInstance = authenticate(username='john', password='secret')
        
        if loginInstance:
            response_data['email'] = loginInstance[0].email
            response_data['status'] = 1
            response_data['token'] = 'token'
        else:
            response_data['status'] = 0

    else:
        response_data['status'] = -1
    
    return JsonResponse(response_data, safe=False)


@csrf_exempt
def join(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('userName')
        password = request.POST.get('password')

        if not email or not name or not password:
            response_data['status'] = 2            
        else:
            
            userInstance = User.objects.create_user(name, email, password)
            userInstance.save()

            obj = UserDetail(user = userInstance, user_type=1)
            print(obj)
            obj.save()


            response_data['email'] = email
            response_data['status'] = 1
            
             
    
    else:
        response_data['status'] = -1
    return JsonResponse(response_data, safe=False)


@csrf_exempt
def logout(request):
    if request.method == "POST":
        email = request.POST.get('email')
        token = request.POST.get('token')

        userInstance = UserDetail.objects.filter(email = email, token = token)
        userInstance.token = ""

        response_data = {
            'status': 1
        }

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
