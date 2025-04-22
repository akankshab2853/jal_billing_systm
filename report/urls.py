# urls.py
from django.urls import path
from .views import generate_excel_report

urlpatterns = [
    path('download-excel/', generate_excel_report, name='download_excel'),
]
