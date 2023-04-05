from rest_framework.generics import (
    ListAPIView,
)
from dry_rest_permissions.generics import DRYPermissions
from django.db.models import Prefetch, Subquery, OuterRef
from django.db import models
from .models import (
    PayrollManagement,
    PayrollInstallments,
)
from .serializers import (
   PayrollManagementSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny


class PayrollList(ListAPIView):
    queryset = PayrollManagement.objects.all()
    serializer_class = PayrollManagementSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return (
                PayrollManagement.objects
                .all()
                .prefetch_related(
                    Prefetch(
                        'payroll_installments',
                        queryset=PayrollInstallments.objects
                        .filter(id__in=Subquery(PayrollInstallments.objects
                        .filter(payroll_management_id=OuterRef('payroll_management_id'))
                        .order_by('-id')
                        .values_list('id', flat=True)[:10]))
                    )
                )

            )
        
        return (
                PayrollManagement.objects
                .all()
                .prefetch_related(
                    Prefetch(
                        'payroll_installments',
                        queryset=PayrollInstallments.objects
                        .filter(id__in=Subquery(PayrollInstallments.objects
                        .filter(payroll_management_id=OuterRef('payroll_management_id'))
                        .filter(payroll_user=user)
                        .values_list('id', flat=True)[:10]))
                    )
                )
        )
    
# model = PayrollManagement
# class PayrollManagement
#    has_many :payroll_installments
# end

# class PayrollInstallments
#     belongs_to :payroll_management
# end

# PayrollManagement.find(1).payroll_installments ( all payrol installments under the payroll managenet with id 1)
# PayrollManagement.find(1).payroll_installments.last ( last payrol installment under the payroll managenet with id 1)
# PayrollManagement.find(1).payroll_installments.last(10) ( last 10 payrol installments under the payroll managenet with id 1)