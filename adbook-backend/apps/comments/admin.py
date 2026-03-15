from django.contrib import admin
from .models import Comment, CommentLike


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'likes_count', 'created_at')
    list_filter = ('created_at',)
    raw_id_fields = ('post', 'parent', 'author')
    search_fields = ('text',)


admin.site.register(CommentLike)
