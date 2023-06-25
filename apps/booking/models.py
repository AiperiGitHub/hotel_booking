from datetime import timedelta
from django.utils import timezone


from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db.models import Q

from apps.hotel.models import Room

User = get_user_model()


class Booking(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='booking',
        verbose_name=_('User'),
        # default=1,
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='booking',
        verbose_name=_('Room'),
    )
    checkin_date = models.DateField(
        _('Checkin date'),
        # default=timezone.now,
        null=True,
        blank=True,
    )
    checkout_date = models.DateField(
        _('Checkout date'),
        # default=timezone.now,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user.username} - {self.room.room_number}"

    def charge(self) -> float:
        return (self.checkout_date - self.checkin_date + timedelta(1)).days * self.room.price

    def clean(self):
        super().clean()
        if self.room_id and self.checkin_date and self.checkout_date:
            existing_booking = Booking.objects.filter(
                room_id=self.room_id,
                checkin_date__lte=self.checkout_date,
                checkout_date__gte=self.checkin_date,
            ).exclude(id=self.id).exists()

            if existing_booking:
                raise ValidationError("Booking for this room and dates already exists.")

    def get_available_rooms(self):
        bookings = Booking.objects.all()
        booked_rooms = bookings.values_list('room_id', flat=True)

        available_rooms = Room.objects.exclude(id__in=booked_rooms)

        # Получаем доступные даты для бронирования
        booked_dates = bookings.values_list('checkin_date', 'checkout_date')
        booked_dates_q = Q()
        for checkin_date, checkout_date in booked_dates:
            booked_dates_q |= Q(checkin_date__range=(checkin_date, checkout_date)) | Q(
                checkout_date__range=(checkin_date, checkout_date))

        available_dates = Booking.objects.exclude(booked_dates_q).values_list('checkin_date', 'checkout_date')

        return available_rooms, available_dates

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")


