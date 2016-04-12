from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from sitemaps import StaticViewSitemap

from blog.sitemaps import BlogIndexSitemap, BlogPostSitemap

admin.autodiscover()

sitemaps = {
    'static': StaticViewSitemap,
    'blog_index': BlogIndexSitemap,
    'blog_posts': BlogPostSitemap,
}

urlpatterns = [
    url(r'^', include('about.urls', namespace='about')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^experience/', include('experience.urls', namespace='experience')),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': sitemaps}
    )
]
