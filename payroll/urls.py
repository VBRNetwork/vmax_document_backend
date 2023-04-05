from django.conf.urls import url
from .views import (
    PayrollList
)

urlpatterns = [
    url(
        r"payroll/$",
        PayrollList.as_view(),
        name="partners",
    ),
]
