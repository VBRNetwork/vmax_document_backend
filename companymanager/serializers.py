from rest_framework import serializers
from .models import (
    TeamMembers,
    Teams,
    Departments,
)
from users.serializers import UserSerializer
from dry_rest_permissions.generics import DRYPermissionsField


class DepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = (
            "id",
            "department_name",
            "department_description"
        )

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = (
            "id",
            "team_name",
            "team_description",
            "team_location",
            "created_at",
        )

class TeamMembersSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    team = TeamsSerializer()
    department = DepartmentsSerializer()

    def to_representation(self, instance):
        self.fields['children'] = TeamMembersSerializer(many=True, read_only=True)
        return super(TeamMembersSerializer, self).to_representation(instance)

    class Meta:
        model = TeamMembers
        fields = (
            "id",
            "user",
            "member_start_date",
            "is_teamleader",
            "is_manager",
            "team",
            "department",
            "organizational_level",
            "member_start_date",
            "member_tenure",
            "children",

        )
