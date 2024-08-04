from django.contrib import admin  # Import Django admin module
from django.urls import path, include, re_path  # Import path, include, and re_path functions for URL routing
from django.conf import settings  # Import settings for configuration
from django.views.static import serve  # Import serve view to serve static files

urlpatterns = [
    # app routing at project level
    path('admin/', admin.site.urls),  # Route for Django admin site
    path('courses/', include('courses.urls')),  # Route for courses app URLs
    path('', include('homepage.urls')),  # Route for homepage app URLs (default)
    path('software/', include('software.urls')),  # Route for software app URLs
    path('themes/', include('themes.urls')),  # Route for themes app URLs
    path('tools/', include('tools.urls')),  # Route for tools app URLs

    # serve static files
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # Route to serve media files
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),  # Route to serve static files
]
