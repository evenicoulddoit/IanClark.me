from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_ianclark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^experience/', include('experience.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
