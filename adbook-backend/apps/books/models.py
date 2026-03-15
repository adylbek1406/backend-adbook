from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from apps.accounts.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='books/covers/')
    publisher = models.CharField(max_length=255, blank=True)
    published_year = models.PositiveSmallIntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_reviews = models.PositiveIntegerField(default=0)
    
    # Full-text search
    search_document = SearchVectorField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['title', 'author']),
            models.Index(fields=['isbn']),
            GinIndex(fields=['search_document']),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1-5
    review_text = models.TextField(blank=True)
    is_verified_purchase = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['book', 'user']),
            models.Index(fields=['book', 'created_at']),
            models.Index(fields=['user', 'created_at']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='unique_book_review')
        ]

