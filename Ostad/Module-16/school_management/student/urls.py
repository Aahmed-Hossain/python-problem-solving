from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='student_profile'),
    path('home/', views.home, name='student_home'),
    path('delete/<int:id>', views.student_delete, name='student_delete'),
]
