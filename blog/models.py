from django.db import models
from django.core.urlresolvers import reverse
import re

class Post(models.Model):
    title = models.CharField("Blog title", max_length=255)
    slug = models.SlugField("Slug (unique)", max_length=255, primary_key=True)
    description = models.CharField("Description (optional)", max_length=255, blank=True)
    tags = models.CharField("Tags (Comma separated)", max_length=150, blank=True)
    created = models.DateTimeField("Creation date", auto_now_add=True)
    published = models.BooleanField("Published", default=True)

    # We store both the markdown content and the generated HTML for caching
    content = models.TextField()
    content_processed = models.TextField()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_tags(self):
        return filter(None, self.tags.split(","))

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])