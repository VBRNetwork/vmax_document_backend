from django.conf.urls import url
from .views import (
    LeaveTypeListView,
    EmployeesLeavesListCreateView,
    UpdateEmployeeLeaves,
)

urlpatterns = [
    url(r"^leave-types/$", LeaveTypeListView.as_view(), name="leave_types"),
    url(
        r"^employees-leaves/$",
        EmployeesLeavesListCreateView.as_view(),
        name="employees_leaves",
    ),
    url(
        r"^employees-leaves/(?P<pk>\d+)/$",
        UpdateEmployeeLeaves.as_view(),
        name="update_employees_leaves",
    )
]