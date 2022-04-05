from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('', include('snippets.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]