from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Defectivestock, Itemstock
from .serializers import DefectivestockSerializer, DefectivestockSerializer, StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Itemstock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['description', 'hsn_code', 'quantity', 'price', 'stock_type']
    search_fields = ['description']  # Enables search functionality by name
    

    def list(self, request, *args, **kwargs):
        try:
            info = Itemstock.objects.all() 
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to add info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to update info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to partially update info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to delete info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

class DefectivestockViewSet(viewsets.ModelViewSet):
    queryset =Defectivestock.objects.all()
    serializer_class = DefectivestockSerializer

    def list(self, request, *args, **kwargs):
        try:
            info = Defectivestock.objects.all() 
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to add info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to update info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to partially update info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'Failed to delete info: {str(e)}'
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)
