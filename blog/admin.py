import re

from blog.templatetags import blog_markdown
from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ("content_processed",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description', 'content']
    list_display = ['title', 'description']
    list_filter = ['published', 'created']

    def save_model(self, request, obj, form, change):
        # Split the tags by any of ;,| and join again using ,. Lowercase values
        tags_processed = filter(None, re.split(r'[;,|]', obj.tags))
        tags_processed = ", ".join(tag.strip().lower() for tag in tags_processed)

        obj.tags = tags_processed

        # Process the content and cache it
        obj.content_processed = blog_markdown.blog_markdown(obj.content)

        # Always make sure a description is added, pull an excerpt from the content if not
        if not obj.description.strip():
            obj.description = obj.get_excerpt()

        obj.save()

admin.site.register(Post, PostAdmin)