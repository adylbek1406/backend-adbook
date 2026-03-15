from django.contrib import admin
from .models import Book, BookReview


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'average_rating', 'total_reviews', 'published_year')
    list_filter = ('published_year',)
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('average_rating', 'total_reviews', 'search_document')


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'is_verified_purchase', 'created_at')
    raw_id_fields = ('book', 'user')
