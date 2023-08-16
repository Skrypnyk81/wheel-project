from django.urls import path
from order.api.views import WheelCreateView, WheelAPIView


urlpatterns = [
    path("create-wheel/", WheelCreateView.as_view(), name="create_wheel"),
    path("retrieve-wheel/<int:pk>/", WheelAPIView.as_view(), name="retrieve_wheel")
]
