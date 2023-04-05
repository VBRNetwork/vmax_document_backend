from tabnanny import verbose
from django.db import models

class Appointments(models.Model):

    id = models.AutoField(primary_key=True)
    appointment_title = models.CharField(max_length=255, blank=True, null=True)
    appointment_description = models.TextField(blank=True, null=True)
    appointment_date = models.CharField(max_length=500, blank=True, null=True)
    appointment_duration = models.CharField(max_length=500, blank=True, null=True)
    appointment_room = models.CharField(max_length=500, blank=True, null=True)
    appointment_customer = models.ForeignKey('users.Customers', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.appointment_title

    class Meta:
        indexes = [
            models.Index(fields=["appointment_title"]),
            models.Index(fields=["id"]),
        ]
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
