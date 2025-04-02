from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import  InvoiceViewset, VendorViewset
urlpatterns = [
    


    path("invoices/", InvoiceViewset.as_view({"get": "list"}), name="invoice-list"),
    path("invoices/create/", InvoiceViewset.as_view({"post": "create"}), name="invoice-create"),
    path("invoices/<int:pk>/", InvoiceViewset.as_view({"get": "retrieve"}), name="invoice-detail"),
    path("invoices/<int:pk>/update/", InvoiceViewset.as_view({"put": "update"}), name="invoice-update"),
    path("invoices/<int:pk>/delete/", InvoiceViewset.as_view({"delete": "destroy"}), name="invoice-delete"),
    
    path('allvendor/', VendorViewset.as_view({'get': 'list'}), name='vendor-list'),
    path('vendordetails/<int:pk>/', VendorViewset.as_view({'get': 'retrieve'}), name='vendor-retrieve'),
    path('addvendor/', VendorViewset.as_view({'post': 'create'}), name='vendor-create'),
    path('updatevendor/<int:pk>/', VendorViewset.as_view({'put': 'update'}), name='vendor-update'),
    path('deletevendor/<int:pk>/', VendorViewset.as_view({'delete': 'destroy'}), name='vendor-delete'),
]

