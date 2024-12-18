from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_subscribed', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_subscribed', 'is_staff', 'is_active')


admin.site.register(User, UserAdmin)

