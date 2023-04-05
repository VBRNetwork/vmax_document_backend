from rest_framework import serializers
from .models import (
    PayrollManagement,
    PayrollInstallments,
)
from users.serializers import UserSerializer, UserProfileSerializer
from dry_rest_permissions.generics import DRYPermissionsField


class PayrollInstallmentsSerializer(serializers.ModelSerializer):

    payroll_installment_file = serializers.FileField(
        max_length=None, allow_empty_file=False, use_url=True
    )

    class Meta:
        model = PayrollInstallments
        fields = (
            "id",
            "payroll_installment_name",
            "payroll_installment_amount_gross",
            "payroll_installment_amount_net",
            "payroll_installment_amount_tax",
            "payroll_installment_amount_deductions",
            "payroll_installment_date",
            "payroll_installment_description",
            "payroll_installment_file",
        )


class PayrollManagementSerializer(serializers.ModelSerializer):

    payroll_user = UserSerializer(many=False, read_only=True)
    payroll_installments = PayrollInstallmentsSerializer(many=True, read_only=True)

    class Meta:
        model = PayrollManagement
        fields = (
            "id",
            "payroll_user",
            "payroll_date_added",
            "payroll_name",
            "payroll_installments",
            "payroll_description",

        )


