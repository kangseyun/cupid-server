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


def board(request):
    if request.method == "POST":
    elif request method == "GET":
    return JsonResponse(response_data, safe=False)
