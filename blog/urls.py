from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

router = routers.DefaultRouter()

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('posts.urls')),
    path(r'', include('revision.urls')),
    path(r'', include('todo.urls')),
    re_path('^rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
