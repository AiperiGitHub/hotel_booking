from django.urls import path, include
from .views import BookingCreateViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'booking', BookingCreateViewSet)


urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('booking/<int:pk>/', BookingCreateViewSet.as_view({'get': 'retrieve'}), name='booking-create'),
] + router.urls




