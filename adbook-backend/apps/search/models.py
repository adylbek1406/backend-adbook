from django.db import models
from django.contrib.postgres.indexes import GinIndex
from apps.books.models import Book
from apps.posts.models import Post


class SearchIndex(models.Model):
    # Global search index for unified search
    searchable_type = models.CharField(max_length=50)  # 'book', 'post', 'user'
    searchable_id = models.PositiveBigIntegerField()
    
    # Search vectors
    title_vector = models.TextField(blank=True)
    content_vector = models.TextField(blank=True)
    tags_vector = models.TextField(blank=True)
    
    # Ranking boost
    popularity_score = models.FloatField(default=1.0)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            GinIndex(fields=['title_vector']),
            GinIndex(fields=['content_vector']),
            GinIndex(fields=['tags_vector']),
        ]


class SearchSuggestion(models.Model):
    query = models.CharField(max_length=255, unique=True)
    suggestion_count = models.PositiveIntegerField(default=0)
    last_searched = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['query']),
        ]

