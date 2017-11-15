from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from api.models import UserDetail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import hashlib
from datetime import datetime
import uuid
from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

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


# def token_check(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if kwargs.get('username') != 'admin':
#             raise Exception("아 진짜 안된다니까 그러네..")
#         return func(*args, **kwargs)
#     return wrapper


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        loginInstance = authenticate(username=username, password=password)
        
        if loginInstance is not None:
            auth_login(request, loginInstance)
            return render(request, 'index.html', {})

        else:
            return render(request, 'login.html', {})    
    return render(request, 'login.html', {})    


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
    # return JsonResponse(response_data, safe=False)
    return render(request, 'join.html', {})


@csrf_exempt
def logout(request):
    if request.method == "GET":
        django_logout(request)
    return redirect('index')
 


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
