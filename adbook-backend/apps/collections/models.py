from django.db import models
from apps.accounts.models import User
from apps.books.models import Book
from apps.posts.models import Post


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    
    item_count = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'is_public']),
            models.Index(fields=['created_at']),
        ]


class SavedItem(models.Model):
    ITEM_TYPES = [
        ('book', 'Book'),
        ('post', 'Post'),
    ]
    
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='items')
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['collection']),
        ]
        ordering = ['order', 'added_at']

