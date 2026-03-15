from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Book, BookReview
from apps.accounts.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('average_rating', 'total_reviews')

class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = BookReview
        fields = '__all__'

