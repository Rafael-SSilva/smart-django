from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CustomUserCreationForm, CustomUserChangeForm
from account.models import Account, UserInfo


class AccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ("first_name", "email", "is_staff", "is_active","is_admin")
    list_filter = ("is_staff", "is_active","is_admin")
    list_per_page = 15
    fieldsets = (
        (None, {"fields": ("first_name","last_name","email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active","groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name","last_name","email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email","first_name", "last_name")
    ordering = ("first_name", "email")


class UserInfoAdmin(admin.ModelAdmin):
    model = UserInfo
    list_display = ("first_name", "email")
    list_per_page = 15
    fieldsets = (
        (None, {"fields": ("first_name","last_name","email")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name","last_name","email",
            )}
        ),
    )
    search_fields = ("email","first_name", "last_name")
    ordering = ("first_name", "email")


admin.site.register(Account, AccountAdmin)
admin.site.register(UserInfo, UserInfoAdmin)