from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^polls/$','index'),
     url(r'^polls/(?P<poll_id>\d+)/$','detail'),
     url(r'^polls/(?P<poll_id>\d+)/results/$','results'),
     url(r'^polls/(?P<poll_id>\d+)/vote/$','vote'),
     url(r'^admin/', include(admin.site.urls)),
)

