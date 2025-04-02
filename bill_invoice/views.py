from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets,status
from bill_invoice.models import Invoice, Vendor
from rest_framework.decorators import api_view

from rest_framework import viewsets
from .models import Invoice, Vendor
from .serializers import InvoiceSerializer, VendorSerializer

# Create your views here.
class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
  
  
def get_queryset(self):
        """Filter invoices based on query parameters (if any)."""
        queryset = Invoice.objects.all()
        vendor_id = self.request.query_params.get('vendor', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if vendor_id:
            queryset = queryset.filter(vendor__id=vendor_id)
        if start_date and end_date:
            queryset = queryset.filter(invoice_date__range=[start_date, end_date])

        return queryset

def list(self, request, *args, **kwargs):
        """Retrieve all invoices with filtering options."""
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All invoices fetched successfully',
                'invoices': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

def retrieve(self, request, *args, **kwargs):
        """Retrieve a single invoice."""
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Invoice retrieved successfully',
                'invoice_details': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

def create(self, request, *args, **kwargs):
        """Create a new invoice."""
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Invoice added successfully',
                'new_invoice': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

def update(self, request, *args, **kwargs):
        """Update an existing invoice."""
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Invoice updated successfully',
                'updated_invoice': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

def partial_update(self, request, *args, **kwargs):
        """Partially update an invoice."""
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Invoice partially updated successfully',
                'updated_invoice': serializer.data
            })
        except Exception as e:
            return self.handle_exception(e)

def destroy(self, request, *args, **kwargs):
        """Delete an invoice."""
        try:
            instance = self.get_object()
            instance.delete()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Invoice deleted successfully'
            })
        except Exception as e:
            return self.handle_exception(e)

def handle_exception(self, e):
        """Handle exceptions."""
        return Response({
            'status': 'error',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
    

class VendorViewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def list(self, request, *args, **kwargs):
        try:
            info = Vendor.objects.all()  
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
