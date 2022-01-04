from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'username', 'last_login', 'is_active', 'sign_up_date', 'last_signin')
    filter_horizontal = ()
    list_filter=()
    fieldsets =()

# Register your models here.
admin.site.register(Account, AccountAdmin)
