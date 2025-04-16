from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Billinvoice, Vendor
from Billinvoice_Items.models import Billinvoiceitems
from .serializers import BillInvoiceSerializer, VendorSerializer
from Billinvoice_Items.serializers import BillItemSerializer

class BillinvoiceAPI(viewsets.ModelViewSet):
          queryset = Billinvoice.objects.prefetch_related('items')
          serializer_class = BillInvoiceSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              info = Billinvoice.objects.all()
                              serializer = self.get_serializer(info, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All info',
                                        'all_info': []
                              }

                              # Manually adjusting response format
                              for invoice in serializer.data:
                                        # Extracting items to a separate field
                                        items = invoice.pop('items', [])
                                        # Adding items to the invoice object at the end
                                        invoice['items'] = items
                                        api_response['all_info'].append(invoice)

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
                              # Extract the Billinvoice data from the request body
                              billinvoice_data = request.data
                              # Deserialize the Billinvoice data
                              billinvoice_serializer = BillInvoiceSerializer(data=billinvoice_data)

                              # Check if the Billinvoice data is valid
                              if billinvoice_serializer.is_valid():
                                        # Save the Billinvoice instance
                                        billinvoice = billinvoice_serializer.save()

                                        # Now handle the items data separately from the request body
                                        items_data = request.data.get('items', [])  # Extract items data if available

                                        for item_data in items_data:
                                                  # Add the invoice_number to each item before saving
                                                  item_data['invoice_number'] = billinvoice.invoice_number
                                                  # Create and save each item
                                                  item_serializer = BillItemSerializer(data=item_data)
                                                  if item_serializer.is_valid():
                                                            item_serializer.save()

                                        # Prepare the response in the desired format
                                        response_data = BillInvoiceSerializer(billinvoice).data
                                        response_data.pop('invoice_number', None)  # Remove invoice_number

                                        # Add the 'items' field to the response
                                        items = Billinvoiceitems.objects.filter(
                                                  invoice_number=billinvoice.invoice_number)
                                        item_serializer = BillItemSerializer(items, many=True)
                                        response_data['items'] = item_serializer.data

                                        # Prepare the final response
                                        api_response = {
                                                  'status': 'success',
                                                  'code': status.HTTP_201_CREATED,
                                                  'message': 'Invoice created successfully',
                                                  'all_info': [response_data]
                                        }

                                        return Response(api_response, status=status.HTTP_201_CREATED)

                              # If the Billinvoice data is not valid, return error
                              return Response(
                                        {'status': 'error', 'message': 'Invalid data',
                                         'errors': billinvoice_serializer.errors},
                                        status=status.HTTP_400_BAD_REQUEST
                              )

                    except Exception as e:
                              error_message = f'An error occurred while creating the invoice: {str(e)}'
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
                              return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

class VendorAPI(viewsets.ModelViewSet):
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
