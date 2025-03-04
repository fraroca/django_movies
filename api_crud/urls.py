
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]

if 'silk' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk'))
   ]