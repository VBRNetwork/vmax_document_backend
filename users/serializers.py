from attr import field
from rest_framework import serializers
from .models import User, UserProfile, ManagerProfile, Roles, Customers
from rest_framework_cache.registry import cache_registry
from main.serializers import CachedSerializerMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer
from dry_rest_permissions.generics import DRYPermissionsField
import re


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
    return re.sub(cleanr, "", raw_html)


class UserSerializer(serializers.ModelSerializer, CachedSerializerMixin):

    class Meta:
        model = User
        ref_name = "User"
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "id",
            "avatar",
            "is_staff",
            "is_superuser",
            "full_name",
        ]
        lookup_field = "username"
        extra_kwargs = {"url": {"lookup_field": "username"}}



class UserDetailedSerializer(
    WritableNestedModelSerializer,
    serializers.ModelSerializer,
    CachedSerializerMixin,
):
    permissions = DRYPermissionsField()

    class Meta:
        model = User
        ref_name = "User Detailed"
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "id",
            "is_staff",
            "is_superuser",
            "permissions",
        ]
        read_only_fields = ["id"]
        lookup_field = "username"
        extra_kwargs = {"url": {"lookup_field": "username"}}

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    role = RolesSerializer(many=False)
    class Meta:
        model = UserProfile
        fields = "__all__"


class ManagerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    role = RolesSerializer(many=False)
    class Meta:
        model = ManagerProfile
        fields = "__all__"

class CustomersSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Customers
        fields = "__all__"




cache_registry.register(UserDetailedSerializer)
cache_registry.register(UserSerializer)