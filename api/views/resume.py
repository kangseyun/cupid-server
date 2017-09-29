from django.http import HttpResponse, JsonResponse
from api.models import Resume
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

response_data = {
    'status': 'token_ok',
    'email': '',
    'token': ''
}


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
