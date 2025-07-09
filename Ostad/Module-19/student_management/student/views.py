from django.shortcuts import render, HttpResponse, redirect
from . import models
from . import forms
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# This is for your html forms
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')
#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False

#         student = models.Student(name=name, email=email, phone=phone, password=password,checkbox=checkbox, photo=photo)

#         student.save()
#         return HttpResponse("Form Submitted.")

#     return render(request, 'student/index.html')


# This is for your ModelForm
def student_list(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES) #request.POST: Contains all the text data submitted in the form and request.FILES: Contains any uploaded files, like images or documents.
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Created Successfully ')
            return redirect('home')
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_update_student.html', {'form': form})



# # Function based view
# def home(request):
#     students = models.Student.objects.all()
#     return render(request, 'student/index.html', {'students': students})

# Class based view
class StudentsList(ListView):
    model = models.Student
    template_name = 'student/index.html'
    context_object_name =  'students'

# def update_student(request, id):
#     student = models.Student.objects.get(id=id)
#     form = forms.StudentForm(instance=student)
#     if request.method == 'POST':
#         form = forms.StudentForm(request.POST, request.FILES, instance=student) #request.POST: Contains all the text data submitted in the form and request.FILES: Contains any uploaded files, like images or documents.
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Student Updated Successfully ')
#             return redirect('home')
#     return render(request, 'student/create_update_student.html', {'form' : form, 'update': True})


# class based view (update)
class UpdateStudent(UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student/create_update_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
         messages.add_message(self.request, messages.SUCCESS, 'Student Updated Successfully ')
         return super().form_valid(form)

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['edit'] = True
        return context


def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Student Deleted Successfully ')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created Successfully')
            return redirect('home')
    else:
        form = forms.SignUpForm()

    return render(request, 'student/auth_form.html', {'form' : form})
