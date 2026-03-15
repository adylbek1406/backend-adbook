from django.contrib import admin
from .models import Post, PostImage, PostShare, PostLike


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'book', 'likes_count', 'comments_count', 'created_at')
    list_filter = ('is_public', 'created_at')
    inlines = [PostImageInline]
    raw_id_fields = ('author', 'book')


admin.site.register([PostImage, PostShare, PostLike])
