from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Device, LoginHistory, OTP


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_email_verified', 'is_phone_verified', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_email_verified')
    search_fields = ('email', 'username', 'phone')
    ordering = ('-date_joined',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'followers_count', 'following_count', 'is_private')
    list_filter = ('is_private',)
    raw_id_fields = ('user',)


admin.site.register([Device, LoginHistory, OTP])
