from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import LeaveType, EmployeesLeaves
from .serializers import LeaveTypeSerializer, EmployeesLeavesSerializer


class LeaveTypeListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    pagination_class = None


class EmployeesLeavesListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = EmployeesLeaves.objects.all()
    serializer_class = EmployeesLeavesSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return EmployeesLeaves.objects.all()
        return EmployeesLeaves.objects.filter(user=self.request.user)
    
class UpdateEmployeeLeaves(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EmployeesLeaves.objects.all()
    serializer_class = EmployeesLeavesSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return EmployeesLeaves.objects.all()
        return None
