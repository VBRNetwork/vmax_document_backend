from django.contrib import admin
from .models import (
    Departments,
    Teams,
    TeamMembers
)

admin.site.register(Departments)
admin.site.register(Teams)
admin.site.register(TeamMembers)