from rest_framework import serializers
from .models import (
    LeaveType,
    EmployeesLeaves,
)
from users.serializers import UserSerializer
from dry_rest_permissions.generics import DRYPermissionsField


class LeaveTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveType
        fields = (
            "id",
            "name",
            "description",
        )


class EmployeesLeavesSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    leave_type = LeaveTypeSerializer(read_only=True)
    handled_by = UserSerializer(read_only=True)

    # def validate(self, data):
    #     validated = super().validate(data)

    #     start_date = validated.get("start_date")
    #     end_date = validated.get("end_date")

    #     if start_date > end_date:
    #         raise serializers.ValidationError(
    #             "Start date must be before end date"
    #         )

    #     return validated

    class Meta:
        model = EmployeesLeaves
        fields = (
            "id",
            "user",
            "leave_type",
            "start_date",
            "end_date",
            "approved_status",
            "handled_by",
            "approved_date",
            "notes",
        )
