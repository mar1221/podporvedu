from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projects.views.index'),
    url(r'^about/', 'projects.views.about'),
    url(r'^contact/', 'projects.views.kontakt'),
    url(r'^support/', 'projects.views.akce'),
    url(r'^project/(?P<project_id>\d+)/$', 'projects.views.projekt', name="project"),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()