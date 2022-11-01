from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "adress", "is_admin")
    search_fields = ("email", "phone_number")
    list_filter = ("is_admin",)


admin.site.register(User, UserAdmin)
