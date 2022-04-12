from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('snippets/', include('snippets.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todo/', include('todo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)