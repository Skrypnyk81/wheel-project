from django.urls import path
from order.api.views import WheelCreateView, WheelAPIView


urlpatterns = [
    path("new-product/", WheelCreateView.as_view(), name="create_wheel"),
    path("retrieve-product/<int:pk>/", WheelAPIView.as_view(), name="retrieve_wheel")
]
