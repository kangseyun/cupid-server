from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from api.models import UserDetail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.

response_data = {
    'status': 'token_ok', 
    'email': '',
    'token': ''
}

@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        loginInstance = User.objects.filter(email=email, password=password)
        
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
            try:
                userInstance = User.objects.create_user(name, email, password)
                userInstance.save()

                obj = UserDetail(user = userInstance)
                obj.save()

                response_data['email'] = email
                response_data['status'] = 1
            except:
                response_data['status'] = -1
    
    else:
        response_data['status'] = -1
    return JsonResponse(response_data, safe=False)