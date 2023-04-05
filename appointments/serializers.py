from rest_framework import serializers
from .models import (
    Appointments,
)
from users.serializers import CustomersSerializer
from dry_rest_permissions.generics import DRYPermissionsField


class AppointmentsSerializer(serializers.ModelSerializer):
    appointment_customer = CustomersSerializer(many=False, read_only=True)
    class Meta:
        model = Appointments
        fields = "__all__"