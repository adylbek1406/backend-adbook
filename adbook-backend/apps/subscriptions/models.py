from django.db import models
from apps.accounts.models import User, Profile
from core.models import TimeStampedModel, SoftDeleteModel


class Follower(TimeStampedModel, SoftDeleteModel):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    is_mutual = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['follower', 'following']),
            models.Index(fields=['following', 'is_mutual']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_follow')
        ]


class Subscription(TimeStampedModel, SoftDeleteModel):
    subscriber = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='subscriptions')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='subscribers')
    notification_types = models.JSONField(default=dict)  # {'new_post': true, 'new_review': false}

    class Meta:
        indexes = [
            models.Index(fields=['subscriber', 'author']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['subscriber', 'author'], name='unique_subscription')
        ]
