from django.db import models
from apps.accounts.models import User
from apps.posts.models import Post
from core.models import TimeStampedModel, SoftDeleteModel


class Comment(TimeStampedModel, SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    text = models.TextField(max_length=1000)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['post', 'created_at']),
            models.Index(fields=['parent']),
            models.Index(fields=['author', 'created_at']),
        ]


class CommentLike(TimeStampedModel, SoftDeleteModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes_from_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_comments')

    class Meta:
        indexes = [
            models.Index(fields=['comment', 'user']),
            models.Index(fields=['comment']),
            models.Index(fields=['user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['comment', 'user'], name='comments_unique_comment_like')
        ]
