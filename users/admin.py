from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django import forms
from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'bio': forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(User, CustomUserAdmin)
