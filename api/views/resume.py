from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Resume, UserDetail, AdTrade, Category, Ads
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import redirect


response_data = {
    'status': 'token_ok',
    'email': '',
    'resume_id': '',
    'token': ''
}


def resume(request):
    # 크리에이터 열람
    if request.method == "GET":
        id = request.GET.get('category', 0)
        category = Category.objects.all()
        if id == 0:
            obj = Resume.objects.all()
            result = [x for x in obj if x.user.status == 3]
        else:
            print("call")
            c = Category.objects.get(id=id)
            obj = Resume.objects.filter(category=c)
            result = [x for x in obj if x.user.status == 3]

        print(obj)
        return render(request, 'resume_list.html', {"category": category, "obj": result})


def resume_regi(request):
    # 크리에이터 열람
    if request.method == "GET":
        user_id = request.GET.get('user')
        try:
            user = UserDetail.objects.get(id=user_id)
            user.status = 3
            user.save()
        except:
            print("fail")
            
        return redirect('my')


def resume_regi_delete(request):
    # 크리에이터 열람
    print("call")
    if request.method == "GET":
        user_id = request.GET.get('user')
        try:
            user = UserDetail.objects.get(id=user_id)
            user.status = 0
            user.save()
        except:
            print("fail")
            
        return redirect('my')


@csrf_exempt
def resume_write(request):
    # 이력서 글 쓰기
    if request.method == "POST":
        email = request.POST.get('email')

        if not email:
            response_data['status'] = 2
        else:
            user_instance = User.objects.get(email=email)
            resume_instance = Resume.objects.create(user=user_instance)
            resume_instance.save()

            response_data['email'] = email
            response_data['status'] = 1

    else:
        response_data['status'] = -1

    return JsonResponse(response_data, safe=False)

def resume_detail(request, id):
    check = 0
    user = UserDetail.objects.get(user = request.user)
    obj = AdTrade.objects.filter(creater = user)
    ad = Ads.objects.get(id=id)

    if len(obj) != 0:
        check = 1

    print(len(obj))
    return render(request, 'resume_result.html', {"call": check,"obj": ad})

# @csrf_exempt
# def resume_detail(request, resume_id):
#     if not resume_id:
#         response_data['status'] = 2
#         return JsonResponse(response_data, safe=False)

#     # 이력서 상세보기
#     if request.method == "GET":
#         return render(request, 'resume_resut.html', {})
#     # 이력서 수정
#     elif request.method == "PUT":
#         resume_instance = Resume.objects.get(id=resume_id)
#         ###########################
#         # 테이블에 컬럼 추가해야 할 듯. 지금 상황에서는 수정할만한 것이 없음
#         ###########################

#         response_data['resume_id'] = resume_instance.id
#         response_data['status'] = 1

#     # 이력서 삭제
#     elif request.method == "DELETE":
#         Resume.objects.filter(id=resume_id).delete()

#         response_data['resume_id'] = resume_id
#         response_data['status'] = 1

#     else:
#         response_data['status'] = -1

#     return JsonResponse(response_data, safe=False)