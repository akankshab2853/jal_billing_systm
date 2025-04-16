    
from django.urls import path
from .views import SupplierViewset
urlpatterns = [
    path('allsupplier',SupplierViewset.as_view({'get':'list'}),name='supplier-list') ,
    path('supplierdetails/<int:pk>/',SupplierViewset.as_view({'get': 'retrieve'}), name='supplier-retrieve'),
    path('addsupplier/', SupplierViewset.as_view({'post': 'create'}), name='supplier-create'),
    path('updatesupplier/<int:pk>/',SupplierViewset.as_view({'put': 'update'}), name='supplier-update'),
    path('deletesupplier/<int:pk>/',SupplierViewset.as_view({'delete': 'destroy'}), name='supplier-delete'),
]
  
  
  