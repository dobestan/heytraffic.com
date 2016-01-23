from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from heytraffic.views import *
from heytraffic.api import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^api/', include([
        url(r'^$', HomeAPIView.as_view(), name='home'),
        url(r'^status/$', StatusAPIView.as_view(), name='status'),
    ], namespace='api', app_name='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
