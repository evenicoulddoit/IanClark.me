from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from sitemaps import StaticViewSitemap

from blog.sitemaps import BlogIndexSitemap, BlogPostSitemap
from ianclark.views import AcmeChallenge


admin.autodiscover()

sitemaps = {
    'static': StaticViewSitemap,
    'blog_index': BlogIndexSitemap,
    'blog_posts': BlogPostSitemap,
}

urlpatterns = [
    url(r'.well-known/acme-challenge/(?P<certbot_id>.+$)',
        AcmeChallenge.as_view(),
        name='acme-challenge'),
    url(r'^', include('about.urls', namespace='about')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^experience/', include('experience.urls', namespace='experience')),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': sitemaps}
    ),
]
