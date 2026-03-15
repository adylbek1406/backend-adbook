from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from drf_spectacular.utils import extend_schema
from .models import Book, BookReview
from .serializers import BookSerializer, BookReviewSerializer

class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Book.objects.all()
    
    @extend_schema(
        description="Список книг"
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
    
    @extend_schema(
        description="Создать книгу"
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        return Book.objects.all()

class BookReviewCreateView(generics.CreateAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_like_toggle(request, id):
    # Like/unlike logic
    return Response({'status': 'liked'})

