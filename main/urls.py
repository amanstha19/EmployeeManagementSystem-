# main/urls.py
from django.urls import path
from .views import home, add_employee, add_doctor, add_patient

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("add-emp/", add_employee, name='add-emp'),  # Add employee page
    path("add-doctor/", add_doctor, name='add-doctor'),  # Add doctor page
    path("add-patient/", add_patient, name="add-patient"),  # Add patient page
]
