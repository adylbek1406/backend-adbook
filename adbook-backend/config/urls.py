from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.accounts.urls')),
    path('api/v1/books/', include('apps.books.urls')),
    # path('api/v1/', include('apps.books.urls')),
    # path('api/v1/', include('apps.posts.urls')),
    # # ... other apps
    path('api/v1/health/', lambda request: {'status': 'healthy'}, name='health'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    import debug_toolbar
#    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

