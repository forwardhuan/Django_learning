from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseBadRequest
import simplejson

from user.models import User


def reg(request):
    print(request)
    print(request.GET)
    print(request.POST)
    print(request.body)

    try:
        payload = simplejson.loads(request.body)
        email = payload['email']

        qs = User.objects.filter(email=1).exists()
        if qs:
            return HttpResponseBadRequest()
        name = payload['name']
        password = payload['password']

        user = User(name=name, password=password, email=email)
        user.save()
        return JsonResponse({'user_id': user.id})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()
