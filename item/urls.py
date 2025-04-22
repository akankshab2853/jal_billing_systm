from django.urls import path
from .views import  DefectivestockViewSet, StockViewSet

urlpatterns = [
    path('allstock/', StockViewSet.as_view({'get': 'list'}), name='stock-list'),
    path('stockdetails/<int:pk>/', StockViewSet.as_view({'get': 'retrieve'}), name='stock-retrieve'),
    path('addstock/', StockViewSet.as_view({'post': 'create'}), name='stock-create'),
    path('updatestock/<int:pk>/', StockViewSet.as_view({'put': 'update'}), name='stock-update'),
    path('deletestock/<int:pk>/', StockViewSet.as_view({'delete': 'destroy'}), name='stock-delete'),
    path('filterstock/', StockViewSet.as_view({'get': 'list'}), name='stock-filter'),
    
    path('DefectiveStock/allstock/',DefectivestockViewSet.as_view({'get': 'list'}), name='stock-list'),
    path('DefectiveStock/stockdetails/<int:pk>/', DefectivestockViewSet.as_view({'get': 'retrieve'}), name='stock-retrieve'),
    path('DefectiveStock/addstock/',DefectivestockViewSet.as_view({'post': 'create'}), name='stock-create'),
    path('DefectiveStock/updatestock/<int:pk>/', DefectivestockViewSet.as_view({'put': 'update'}), name='stock-update'),
    path('DefectiveStock/deletestock/<int:pk>/',DefectivestockViewSet.as_view({'delete': 'destroy'}), name='stock-delete'),
]
    
