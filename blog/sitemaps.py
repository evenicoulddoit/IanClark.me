from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from models import Post

class BlogIndexSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['blog.views.index',]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        obj.created
