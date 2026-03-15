from django.db import models
from django.contrib.postgres.indexes import GinIndex
from apps.accounts.models import User, Profile
from apps.books.models import Book
from core.models import TimeStampedModel, SoftDeleteModel


class Post(TimeStampedModel, SoftDeleteModel):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    caption = models.TextField(max_length=2000, blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    is_public = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['author', 'created_at']),
            models.Index(fields=['book']),
            GinIndex(fields=['caption']),
        ]
        ordering = ['-created_at']


class PostImage(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/images/')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['post', 'order']),
        ]
        ordering = ['order']


class PostShare(TimeStampedModel, SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='shares')
    sharer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='shared_posts')
    shared_to_feed = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['post', 'sharer']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['post', 'sharer'], name='unique_post_share')
        ]


class PostLike(TimeStampedModel, SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes_from_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')

    class Meta:
        indexes = [
            models.Index(fields=['post', 'user']),
            models.Index(fields=['post']),
            models.Index(fields=['user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='posts_unique_post_like')
        ]
