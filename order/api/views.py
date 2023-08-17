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
