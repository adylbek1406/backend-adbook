from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListCreateView.as_view(), name='list_create'),
    path('<int:id>/', views.BookDetailView.as_view(), name='detail'),
    path('<int:id>/like/', views.book_like_toggle, name='like'),
    path('<int:id>/review/', views.BookReviewCreateView.as_view(), name='review'),
]

