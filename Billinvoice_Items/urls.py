from django.urls import path

from Billinvoice_Items.views import BillItemAPI

urlpatterns = [
          path('allitems/', BillItemAPI.as_view({'get': 'list'})),
          path('itemdetails/<int:pk>/', BillItemAPI.as_view({'get': 'retrieve'})),
          path('additem/', BillItemAPI.as_view({'post': 'create'})),
          path('updateitem/<int:pk>/', BillItemAPI.as_view({'put': 'update'})),
          path('partialupdateitem/<int:pk>/', BillItemAPI.as_view({'patch': 'partial_update'})),
          path('deleteitem/<int:pk>/', BillItemAPI.as_view({'delete': 'destroy'})),

]
