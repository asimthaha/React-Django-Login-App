from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.db.models import Q

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        getUsername = data['name']
        getPassword = data['password']
        loginData = UserRegistrationModel.objects.filter(Q(name__exact=getUsername) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))