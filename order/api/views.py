from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from order.models import Wheel, Order
from order.api.serializers import WheelSerializers, WheelListSerializers, OrderSerializers
from rest_framework import permissions


class WheelCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = WheelSerializers
    permission_classes = [permissions.IsAdminUser]


class WheelAPIView(GenericAPIView):
    serializer_class = WheelSerializers
    queryset = Wheel.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class WheelsListAPIView(ListAPIView):
    serializer_class = WheelListSerializers
    queryset = Wheel.objects.all()


class FilterListAPIView(APIView):

    @staticmethod
    def post(request, format=None):
        filter_wheel = request.data
        filter_result = Wheel.objects.filter(**filter_wheel)
        serializer = WheelListSerializers(filter_result, many=True)
        return Response(serializer.data)


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def perform_create(self, serializer):
        # Salviamo l'ordine nel database
        order = serializer.save()

        wheel_instance = Wheel.objects.get(id=order.wheel_id)
        wheel_instance.on_sale = False
        wheel_instance.save()

        # Inviamo un'email dopo la creazione
        self.send_order_email(order)

    def send_order_email(self, order):
        # Definisci il mittente, il destinatario e il contenuto dell'email
        subject = f'Grazie per il tuo ordine delle gomme {order.wheel.brand}!'
        message = 'Il tuo ordine è stato ricevuto e verrà elaborato a breve.'
        from_email = 'gomme-usate@skrypnyk81.it'
        recipient_list = [order.email]  # Assumendo che "email" sia un campo del tuo modello Order

        # Invia l'email
        send_mail(subject, message, from_email, recipient_list)