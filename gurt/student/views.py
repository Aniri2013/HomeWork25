from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
def index(request):
   # print()
   # print(student)
   # print()
  # print()

   student = Student.objects.all()
   return render(request, "student/student.html", context={"student": student})
