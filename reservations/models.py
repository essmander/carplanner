from django.db import models

from django.contrib.auth.models import User
from django.db.models import Q


class ReservationsQuerySet(models.QuerySet):
    def reservations_for_user(self, user):
        return self.filter(
            Q(user_reservation=user)
        )

class Reservation(models.Model):
    user_reservation = models.ForeignKey(User, blank=False, related_name="reservation", on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    customer = models.CharField(max_length=50)
    project_number = models.CharField(max_length=50)

    objects = ReservationsQuerySet.as_manager()

    def __str__(self):
        return f"You have a reservation from {self.date_from} at {self.start_time}. To {self.date_to} at {self.date_from}. Viseting customer {self.customer} ({self.project_number})"