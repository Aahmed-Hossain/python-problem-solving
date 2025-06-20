from django.shortcuts import render
from django.http import HttpResponse
from . import models

def profile(request):
    user_data = {
        'name': 'Rahim',
        'age': 20
    }
    marks = [
        {   "id":1,
            "subject": "English",
            "marks": 89
        },
        {   "id":2,
            "subject": "Math",
            "marks": 67
        },
        {   "id":3,
            "subject": "Computer",
            "marks": 99
        },
        {   "id":4,
            "subject": "Zology",
            "marks": 79
        },
    ]
    student_data = models.Student.objects.all()
    blog_data = models.Blog.objects.all()

    return render(request, 'student/index.html', {
    "student_data": student_data,
    "blog_data": blog_data,
    "marks": marks
    })

def home(request):
    return HttpResponse('<h1> I am from student home </h1>')

def student_delete(request,id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return HttpResponse('Student Deleted Succesfully')
