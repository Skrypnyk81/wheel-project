from rest_framework import serializers
from order.models import WheelsImage, Wheel


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
        fields = ["id", "width", "ratio", "diameter", "price", "load", "speed", "season", "brand", "runflat", "dot",
                  "reinforced", "load_c", "on_sale", "images", "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        wheel = Wheel.objects.create(**validated_data)

        for image in uploaded_images:
            WheelsImage.objects.create(wheel=wheel, image=image)

        return wheel
