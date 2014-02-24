from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description', 'content']
    list_display = ['title', 'description']
    list_filter = ['published', 'created']

admin.site.register(Post, PostAdmin)