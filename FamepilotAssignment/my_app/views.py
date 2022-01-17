import json
import math

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from .serializers import RegisterSerializer, LoginSerializer


class Index(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'index.html')


class Register(View):
    def get(self, *args, **kwargs):
        serializer = RegisterSerializer()
        return render(self.request, 'register.html', {'serializer': serializer})

    def post(self, *args, **kwargs):
        serializer = RegisterSerializer(data=self.request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('my_app:login')
        return redirect('my_app:register')


class Login(View):
    def get(self, *args, **kwargs):
        serializer = LoginSerializer()
        return render(self.request, 'login.html', {'serializer': serializer})

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                auth_login(self.request, user)
                return redirect('my_app:index')
        return redirect('my_app:login')


class Logout(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            auth_logout(self.request)
        return redirect('my_app:login')


def get_keys(val, dict):
    array = []
    for key, value in dict.items():
        if value == val:
            array.append(key)
    return array


def group_by_owners(request):
    if request.method == 'POST':
        input_dict = request.POST.get('dict')
        output_dict = {}
        try:
            res = json.loads(input_dict)
        except:
            return JsonResponse({
                'Status': False,
                'Message': "Please check the syntax and try again!..."
            })
        for key, value in res.items():
            if output_dict.get(value) is None:
                output_dict[value] = get_keys(value, res)

        return JsonResponse({
            'Status': True,
            'dict': output_dict
        })


def find_roots(a, b, c):
    d = (b * b) - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    return (sol1, sol2)


class QuadraticRoots(View):
    def post(self, *args, **kwargs):
        a = int(self.request.POST.get('a'))
        b = int(self.request.POST.get('b'))
        c = int(self.request.POST.get('c'))
        ans = find_roots(a, b, c)
        return JsonResponse({
            'Status': True,
            'answer': ans
        })
