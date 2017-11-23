from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from api.models import Ads, Category


def index(request):
    return render(request, './index.html', {})

def my(request):
    return render(request, './my/index.html', {})


def chat(requset):
    return render(requset, './my/chat.html', {})


def notification(requset):
    return render(requset, './my/notification.html', {})

def ad_write(requset):
    if requset.method == "POST":
        budget = requset.POST.get("budget")
        subject = requset.POST.get("subject")
        content = requset.POST.get("content")
        category = requset.POST.get("category")
        Ads()
        print(budget, subject, content, category)

        return redirect('ad_write')
    elif requset.method == "GET":
        category = Category.objects.all()
        print(category)
        return render(requset, './my/ad_write.html', {'category': category})
