from django.conf.urls import url
from .views import (
    HrFilesList,
    HrFileRequestCreateList,
    RecruitmentLeadsCreateList,
    RecruitmentLeadsRetreiveUpdateDestroy,
)


urlpatterns = [
    url(
        r"hr-files/$",
        HrFilesList.as_view(),
        name="hr_files",
    ),
    url(
        r"hr-files-requests/$",
        HrFileRequestCreateList.as_view(),
        name="hr_files_requests",
    ),
    url(
        r"recruitments/$",
        RecruitmentLeadsCreateList.as_view(),
        name="recruitments",
    ),
    url(
        r"recruitments/update/(?P<pk>\d+)$",
        RecruitmentLeadsRetreiveUpdateDestroy.as_view(),
        name="recruitments",
    ),
]
