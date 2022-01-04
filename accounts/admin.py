from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'username', 'is_active', 'sign_up_date', 'last_signin')
    list_display_links = ('email', 'first_name')
    readonly_fields = ('last_signin', 'sign_up_date')
    ordering = ('sign_up_date', )
    filter_horizontal = ()
    list_filter=()
    fieldsets =()

# Register your models here.
admin.site.register(Account, AccountAdmin)
