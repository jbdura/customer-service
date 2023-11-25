# messaging/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Message, Response
from .serializers import MessageSerializer, ResponseSerializer
from accounts.models import Customer
from accounts.serializers import CustomerSerializer


class CustomerMessagesView(APIView):
    def get(self, request, customer_pk, *args, **kwargs):
        try:
            customer = Customer.objects.get(pk=customer_pk)
            messages = Message.objects.filter(customer=customer)
            serializer = MessageSerializer(messages, many=True)
            customer_data = CustomerSerializer(customer).data
            response_data = {
                'customer': customer_data,
                'messages': serializer.data
            }
            return Response(response_data)
        except Customer.DoesNotExist:
            return Response({'detail': 'Customer not found'}, status=404)


class AnswerMessageView(APIView):
    def post(self, request, customer_pk, *args, **kwargs):
        try:
            customer = Customer.objects.get(pk=customer_pk)
            message_id = request.data.get('message_id')
            message = Message.objects.get(id=message_id, customer=customer, reply=None)

            # Assuming the agent's reply is sent in the request data
            agent_reply_content = request.data.get('agent_reply_content', '')

            # Create a new Response object as the agent's reply
            response = Response.objects.create(
                content=agent_reply_content,
                message=message
            )

            # Associate the Response with the original Message as a reply
            message.reply = response  # Fix the typo here (it was 'message. Reply')
            message.save()

            return Response({'detail': 'Message answered successfully'})
        except Customer.DoesNotExist:
            return Response({'detail': 'Customer not found'}, status=404)
        except Message.DoesNotExist:
            return Response({'detail': 'Message not found or already answered'}, status=404)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

#######################################################################################################################


# # messaging/views.py
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from .models import Message, Response
# from .serializers import MessageSerializer, ResponseSerializer
# from accounts.models import Customer
# from accounts.serializers import CustomerSerializer
#
#
# class CustomerMessagesView(APIView):
#     def get(self, request, customer_pk, *args, **kwargs):
#         try:
#             customer = Customer.objects.get(pk=customer_pk)
#             messages = Message.objects.filter(customer=customer)
#             serializer = MessageSerializer(messages, many=True)
#             customer_data = CustomerSerializer(customer).data
#             response_data = {
#                 'customer': customer_data,
#                 'messages': serializer.data
#             }
#             return Response(response_data)
#         except Customer.DoesNotExist:
#             return Response({'detail': 'Customer not found'}, status=404)
#
#
# class AnswerMessageView(APIView):
#     def post(self, request, customer_pk, *args, **kwargs):
#         try:
#             customer = Customer.objects.get(pk=customer_pk)
#             message_id = request.data.get('message_id')
#             message = Message.objects.get(id=message_id, customer=customer, reply=None)
#
#             # Assuming the agent's reply is sent in the request data
#             agent_reply_content = request.data.get('agent_reply_content', '')
#
#             # Create a new Response object as the agent's reply
#             response = Response.objects.create(
#                 content=agent_reply_content,
#                 message=message
#             )
#
#             # Associate the Response with the original Message as a reply
#             message.reply = response
#             message.save()
#
#             return Response({'detail': 'Message answered successfully'})
#         except Customer.DoesNotExist:
#             return Response({'detail': 'Customer not found'}, status=404)
#         except Message.DoesNotExist:
#             return Response({'detail': 'Message not found or already answered'}, status=404)
#
#
#
#
########################################################################################################################
# # from django.shortcuts import render
# # from rest_framework import viewsets
# # from .models import Message, Response
# # from .serializers import MessageSerializer, ResponseSerializer
# #
# #
# # Create your views here.
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#
# class ResponseViewSet(viewsets.ModelViewSet):
#     queryset = Response.objects.all()
#     serializer_class = ResponseSerializer
