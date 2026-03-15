from django.db import models
from apps.accounts.models import User
from apps.posts.models import Post
from apps.comments.models import Comment


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes_from_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['post']),
            models.Index(fields=['user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='likes_unique_post_like')
        ]


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_likes')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['comment']),
            models.Index(fields=['user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['comment', 'user'], name='likes_unique_comment_like')
        ]

