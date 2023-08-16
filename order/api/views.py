from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from order.models import Wheel
from order.api.serializers import WheelSerializers


class WheelCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = WheelSerializers


class WheelAPIView(GenericAPIView):
    serializer_class = WheelSerializers
    queryset = Wheel.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
