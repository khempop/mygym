from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Gym
class UserAdmin(BaseUserAdmin):
    #form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (('Info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
            (('user_info'), {'fields': ('title', 'stripeid','code','status')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'title', 'stripeid','code','status']
    search_fields = ('email', 'first_name', 'last_name', 'stripeid','code',)
    ordering = ('email', )
admin.site.register(Gym, UserAdmin)