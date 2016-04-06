from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField("Blog title", max_length=255)
    slug = models.SlugField("Slug (unique)", max_length=255, primary_key=True)
    description = models.CharField(
        "Description", max_length=255, blank=True)
    tags = models.CharField(
        "Tags (Comma separated)", max_length=150, blank=True)
    created = models.DateTimeField("Creation date", auto_now_add=True)
    published = models.BooleanField("Published", default=True)

    # We store both the markdown content and the generated HTML for caching
    content = models.TextField()
    content_processed = models.TextField()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_excerpt(self):
        """Return an excerpt of the article's content."""

        if self.content_processed:
            soup = BeautifulSoup(self.content_processed)

            for tag in soup.findAll(True):
                if (
                    tag.name == "table" and
                    "code-snippettable" in tag.get("class", [])
                ):
                    tag.decompose()
                elif tag.name:
                    tag.unwrap()

            description = " ".join(soup.prettify().split())

            if len(description) > 252:
                return description[:252] + "..."
            else:
                return description

    def get_absolute_url(self):
        return reverse('blog:post', args=(self.slug,))

    @property
    def tags_filtered(self):
        return filter(None, self.tags.split(","))
