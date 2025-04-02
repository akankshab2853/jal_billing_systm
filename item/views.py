from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Stock
from .serializers import StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'hsn_code', 'quantity', 'price', 'stock_type']
    search_fields = ['name']  # Enables search functionality by name

    def get_queryset(self):
        queryset = Stock.objects.all()
        stock_type = self.request.query_params.get('stock_type', None)

        if stock_type:
            queryset = queryset.filter(stock_type=stock_type.lower())  # Ensures lowercase comparison

        return queryset

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All stock items fetched successfully',
                'all_stock': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Stock item retrieved successfully',
                'stock_details': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

    def create(self, request, *args, **kwargs):
        try:
            request.data['stock_type'] = request.data['stock_type'].lower()  # Convert to lowercase
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Stock item added successfully',
                'new_stock': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

    def update(self, request, *args, **kwargs):
        try:
            request.data['stock_type'] = request.data['stock_type'].lower()  # Convert to lowercase
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Stock item updated successfully',
                'updated_stock': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

    def partial_update(self, request, *args, **kwargs):
        try:
            if 'stock_type' in request.data:
                request.data['stock_type'] = request.data['stock_type'].lower()  # Convert to lowercase
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Stock item partially updated successfully',
                'updated_stock': serializer.datas
            })
        except Exception as e:
            return self.handle_exception(e)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Stock item deleted successfully'
            })
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, e):
        return Response({
            'status': 'error',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
