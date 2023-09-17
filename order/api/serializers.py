from rest_framework import serializers
from order.models import WheelsImage, Wheel, Order


class WheelsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = WheelsImage
        fields = "__all__"


class WheelSerializers(serializers.ModelSerializer):
    images = WheelsImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Wheel
        exclude = ["on_sale", "created_at"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        wheel = Wheel.objects.create(**validated_data)

        for image in uploaded_images:
            WheelsImage.objects.create(wheel=wheel, image=image)

        return wheel


class WheelListSerializers(serializers.ModelSerializer):
    images = WheelsImageSerializers(many=True, read_only=True)

    class Meta:
        model = Wheel
        fields = ["id", "brand", "width", "ratio", "diameter", "tread", "price", "images"]


class OrderSerializers(serializers.ModelSerializer):
    wheel = serializers.PrimaryKeyRelatedField(queryset=Wheel.objects.all())

    class Meta:
        model = Order
        fields = "__all__"
