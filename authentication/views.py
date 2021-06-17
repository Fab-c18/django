from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')

class UsernameValView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Enter proper username.'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Username already exists'},status=409)
        return JsonResponse({'valid_username': True}) 