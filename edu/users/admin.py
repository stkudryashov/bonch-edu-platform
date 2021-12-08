from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext_lazy as _

from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
    )

    filter_horizontal = ('user_permissions',)
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(User, MyUserAdmin)
