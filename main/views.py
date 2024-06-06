from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, "main/home.html")




def add_employee(request):
    return render(request,'main/add_emp.html')

def add_doctor(request):
    
    return render(request, 'main/add_doctor.html')


def add_patient(request):
    
    return render(request, 'main/add_patient.html')

