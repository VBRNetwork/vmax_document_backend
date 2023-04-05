from django.conf.urls import url
from .views import (
    AppointmentsCreateList,
)

urlpatterns = [
    url(
        r"appointments/$",
        AppointmentsCreateList.as_view(),
        name="hr_files",
    ),
]
