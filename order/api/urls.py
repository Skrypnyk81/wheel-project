from django.urls import path
from order.api.views import WheelCreateView, WheelAPIView, WheelsListAPIView, FilterListAPIView


urlpatterns = [
    path("create-wheel/", WheelCreateView.as_view(), name="create_wheel"),
    path("detail-wheel/<int:pk>/", WheelAPIView.as_view(), name="detail_wheel"),
    path("list-wheel/", WheelsListAPIView.as_view(), name="retrieve_wheel"),
    path("filter-list-wheel/", FilterListAPIView.as_view(), name="retrieve_wheel"),
]
