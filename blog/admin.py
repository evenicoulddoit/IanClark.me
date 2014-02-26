from blog.templatetags import blog_markdown
from django.contrib import admin
from blog.models import Post
import re

class PostAdmin(admin.ModelAdmin):
    exclude = ("content_processed",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description', 'content']
    list_display = ['title', 'description']
    list_filter = ['published', 'created']

    def save_model(self, request, obj, form, change):
        tags_processed = filter(None, re.split(r'[;,|]', obj.tags))
        tags_processed = ", ".join(tag.strip().lower() for tag in tags_processed)

        obj.tags = tags_processed

        # Process the content and cache it
        obj.content_processed = blog_markdown.blog_markdown(obj.content)
        obj.save()

admin.site.register(Post, PostAdmin)