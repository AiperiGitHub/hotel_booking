from django.urls import path, include
from .views import BookingCreateViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'bookig', BookingCreateViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),

]






