from django.db import models
from apps.accounts.models import User
from apps.accounts.models import User


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('like', 'Post Like'),
        ('comment', 'Comment'),
        ('follow', 'New Follower'),
        ('mention', 'Mention'),
        ('share', 'Post Share'),
        ('chat_message', 'New Chat Message'),
        ('book_review_reply', 'Review Reply'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=30, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    
    # Related objects (polymorphic)
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sent_notifications')
    related_post_id = models.PositiveBigIntegerField(null=True, blank=True)
    related_comment_id = models.PositiveBigIntegerField(null=True, blank=True)
    
    is_read = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'is_read', 'created_at']),
            models.Index(fields=['notification_type']),
        ]
        ordering = ['-created_at']


class NotificationPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notification_prefs')
    
    # Email preferences
    email_like = models.BooleanField(default=True)
    email_comment = models.BooleanField(default=True)
    email_follow = models.BooleanField(default=True)
    
    # Push preferences
    push_like = models.BooleanField(default=True)
    push_comment = models.BooleanField(default=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]

