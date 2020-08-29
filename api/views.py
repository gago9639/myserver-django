from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
import json


def index(request):
    return render(request, "index.html")

def login(request):
    data = json.loads(request.body)
    user = authenticate(request, username=data['username'], password=data['password'])

    if user is not None:
        res = {
            'first_name': user.first_name,
            'last_name': user.last_name}
    else:
        res = {'res': 'INVALID'}

    return JsonResponse(res)


def register(request):
    data = json.loads(request.body)
    user = User.objects.create_user(username=data['username'], password=data['password'], 
                                    first_name=data['first_name'], last_name=data['last_name'])
    
    return JsonResponse({'username': user.username})
