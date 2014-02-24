from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', locals())

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', locals())