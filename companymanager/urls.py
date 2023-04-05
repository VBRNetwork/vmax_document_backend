from django.conf.urls import url
from .views import (
    TeamsList,
    DepartmentsList,
    TeamMembersList,
    LastTeam,
)


urlpatterns = [
    url(
        r"teams/$",
        TeamsList.as_view(),
        name="partners",
    ),
    url(
        r"departments/$",
        DepartmentsList.as_view(),
        name="contracts",
    ),
    url(
        r"team-members/$",
        TeamMembersList.as_view(),
        name="team_members",
    ),
    url(
        r"last-team/$",
        LastTeam.as_view(),
        name="last_team",
    ),
    # url(
    #     r"last-team/(?P<pk>\d+)$",
    #     LastTeam.as_view(),
    #     name="last_team",
    # ),
]
