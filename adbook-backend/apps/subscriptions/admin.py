from django.contrib import admin
from .models import Follower, Subscription


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'is_mutual', 'created_at')
    list_filter = ('is_mutual',)
    raw_id_fields = ('follower', 'following')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'author', 'created_at')
    raw_id_fields = ('subscriber', 'author')
