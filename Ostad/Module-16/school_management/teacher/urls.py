from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='teacher_profile'),
    path('home/', views.home, name='teacher_home'),
]
