from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ( 'username', 'email', 'phone_number', 'role', 'address', 'profile_picture')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ( 'email', 'password')}),
        ('Personal info', {'fields': ('username', 'phone_number', 'address', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'address', 'profile_picture')}
        ),
    )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, UserAdmin)