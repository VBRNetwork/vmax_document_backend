from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from dry_rest_permissions.generics import DRYPermissions
from .models import (
    Teams,
    Departments,
    TeamMembers,
)
from .serializers import (
    TeamsSerializer,
    DepartmentsSerializer,
    TeamMembersSerializer,
)
from rest_framework.permissions import IsAuthenticated, AllowAny


class TeamsList(ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class DepartmentsList(ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class TeamMembersList(ListAPIView):
    queryset = TeamMembers.objects.filter(parent=None).all()
    serializer_class = TeamMembersSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class LastTeam(ListAPIView):
    queryset = Teams.objects.order_by('-id')[:1]
    serializer_class = TeamsSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    lookup_field = "id"
    lookup_url_kwarg = "id"
