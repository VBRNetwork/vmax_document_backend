from django.contrib import admin
from .models import User, UserProfile, ManagerProfile, Roles, Customers


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(ManagerProfile)
admin.site.register(Roles)
admin.site.register(Customers)
