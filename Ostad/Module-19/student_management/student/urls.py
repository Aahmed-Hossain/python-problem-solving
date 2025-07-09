from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),  # function based view
    path('home/', views.StudentsList.as_view(), name='home'),  # class based view
    path('create/', views.student_list, name='create_student'),
    # path('update/<int:id>', views.update_student, name='update_student'), # function based view (update)
    path('update/<int:id>', views.UpdateStudent.as_view(), name='update_student'), # class based view (update)
    path('delete/<int:id>', views.delete_student, name='delete_student'),
    path('signup/', views.signup, name='signup'),
]
