from django.urls import path
from bill_invoice.views import VendorAPI, BillinvoiceAPI

urlpatterns = [
          path('allBillInvoices/', BillinvoiceAPI.as_view({"get": "list"}), name="BillInvoice-list"),
          path("addBillInvoices/create/", BillinvoiceAPI.as_view({"post": "create"}), name="BillInvoice-create"),
          path("BillInvoices/<int:pk>/", BillinvoiceAPI.as_view({"get": "retrieve"}), name="-detailBillInvoice"),
          path("updateBillInvoices/<int:pk>/", BillinvoiceAPI.as_view({"put": "update"}),
               name="BillInvoice-update"),
          path("deleteBillInvoices/<int:pk>/", BillinvoiceAPI.as_view({"delete": "destroy"}),
               name="BillInvoice-delete"),

          path('allvendor/', VendorAPI.as_view({'get': 'list'}), name='vendor-list'),
          path('vendordetails/<int:pk>/', VendorAPI.as_view({'get': 'retrieve'}), name='vendor-retrieve'),
          path('addvendor/', VendorAPI.as_view({'post': 'create'}), name='vendor-create'),
          path('updatevendor/<int:pk>/', VendorAPI.as_view({'put': 'update'}), name='vendor-update'),
          path('deletevendor/<int:pk>/', VendorAPI.as_view({'delete': 'destroy'}), name='vendor-delete')

]
