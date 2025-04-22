from django.urls import path
from bill_invoice.views import VendorAPI, BillinvoiceAPI

urlpatterns = [
          path('bill/allBillInvoices/', BillinvoiceAPI.as_view({"get": "list"}), name="BillInvoice-list"),
          path("bill/addBillInvoices/create/", BillinvoiceAPI.as_view({"post": "create"}), name="BillInvoice-create"),
          path("bill/BillInvoices/<int:pk>/", BillinvoiceAPI.as_view({"get": "retrieve"}), name="-detailBillInvoice"),
          path("bill/updateBillInvoices/<int:pk>/", BillinvoiceAPI.as_view({"put": "update"}),name="BillInvoice-update"),
          path("bill/deleteBillInvoices/<int:pk>/", BillinvoiceAPI.as_view({"delete": "destroy"}),name="BillInvoice-delete"),

          path('vendor/allvendor/', VendorAPI.as_view({'get': 'list'}), name='vendor-list'),
          path('vendor/vendordetails/<int:pk>/', VendorAPI.as_view({'get': 'retrieve'}), name='vendor-retrieve'),
          path('vendor/addvendor/', VendorAPI.as_view({'post': 'create'}), name='vendor-create'),
          path('vendor/updatevendor/<int:pk>/', VendorAPI.as_view({'put': 'update'}), name='vendor-update'),
          path('vendor/deletevendor/<int:pk>/', VendorAPI.as_view({'delete': 'destroy'}), name='vendor-delete')
]