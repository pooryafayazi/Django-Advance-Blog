from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User,Profile

class customUserAdmin(UserAdmin):
    model = User   
    list_display = ['email', 'is_superuser', 'is_active']
    list_filter = ['is_superuser', 'is_active']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
                ("Authentication", {'fields': ('email', 'password')}),
                ('Permissions', {'fields': ('is_staff','is_superuser', 'is_active')}),
                ('groups permissions', {'fields': ('groups','user_permissions')}),
                ('Important dates', {'fields': ('last_login',)}),
                )
    add_fieldsets = (
                ('Authentication', {'fields': ('email', 'password1', 'password2')}),
                ('Permissions', {'fields': ('is_staff','is_superuser', 'is_active')}),                
                )

admin.site.register(Profile)
admin.site.register(User, customUserAdmin)
