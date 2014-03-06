from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.sitemaps import BlogIndexSitemap, BlogPostSitemap
from sitemaps import StaticViewSitemap

admin.autodiscover()

sitemaps = {
    'static': StaticViewSitemap,
    'blog_index': BlogIndexSitemap,
    'blog_posts': BlogPostSitemap,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_ianclark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('about.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^experience/', include('experience.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
