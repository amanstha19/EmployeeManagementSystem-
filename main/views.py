from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp(request):
    return render(request, "main/home.html")