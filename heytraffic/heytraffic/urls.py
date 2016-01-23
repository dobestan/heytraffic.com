from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from heytraffic.views import *
from heytraffic.api import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^', include([
        url(r'^traffic/$', TrafficServiceView.as_view(), name='traffic'),
        url(r'^facebook/$', FacebookServiceView.as_view(), name='facebook'),
        url(r'^twitter/$', TwitterServiceView.as_view(), name='twitter'),
        url(r'^instagram/$', InstagramServiceView.as_view(), name='instagram'),
        url(r'^youtube/$', YoutubeServiceView.as_view(), name='youtube'),
    ], namespace='service', app_name='service')),

    url(r'^api/', include([
        url(r'^$', HomeAPIView.as_view(), name='home'),
        url(r'^status/$', StatusAPIView.as_view(), name='status'),
    ], namespace='api', app_name='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
