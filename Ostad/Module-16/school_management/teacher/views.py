from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    user_data = {
        'name': 'Karim Sir',
        'age': 20
    }
    return render(request, 'teacher/index.html', user_data)

def home(request):
    return HttpResponse('<h1> I am from teacher home </h1>')
