# authentication/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the list of fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'roll', 'is_staff', 'is_superuser')

    # Add filters for easy searching in the admin
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'roll')

    # Define the fieldsets to use in the admin add/edit pages
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Custom Fields', {'fields': ['roll']}),  # Add any additional custom fields here
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add any custom inlines here if needed
    # inlines = []

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
