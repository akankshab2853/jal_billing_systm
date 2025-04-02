    
from django.urls import path
from .views import SupplierViewset
urlpatterns = [
    path('allsupplier',SupplierViewset.as_view({'get':'list'}),) ,
    path('supplierdetails/<int:pk>/',SupplierViewset.as_view({'get': 'retrieve'}), name='vendor-retrieve'),
    path('addsupplier/', SupplierViewset.as_view({'post': 'create'}), name='vendor-create'),
    path('updatesupplier/<int:pk>/',SupplierViewset.as_view({'put': 'update'}), name='vendor-update'),
    path('deletesupplier/<int:pk>/',SupplierViewset.as_view({'delete': 'destroy'}), name='vendor-delete'),
]
  
  
  