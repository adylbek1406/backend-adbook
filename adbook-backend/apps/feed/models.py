from django.db import models
from apps.accounts.models import User
from apps.posts.models import Post


class FeedCache(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_cache')
    feed_type = models.CharField(
        max_length=20,
        choices=[('personalized', 'Personalized'), ('explore', 'Explore')],
        default='personalized'
    )
    
    # JSONField stores ordered post IDs
    post_ids = models.JSONField()
    
    expires_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'feed_type']),
            models.Index(fields=['expires_at']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'feed_type'], name='unique_user_feed')
        ]


class FeedInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feed_interactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    # ML features for ranking
    score = models.FloatField()
    interaction_type = models.CharField(max_length=20)  # view, like, comment
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'post']),
            models.Index(fields=['score']),
        ]

