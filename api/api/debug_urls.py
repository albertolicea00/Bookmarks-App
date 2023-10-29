# urls.py

from django.conf import settings
from django.urls import include, path
import debug_toolbar


urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
