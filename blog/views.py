from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.filter(published=True)
    page_title = "Blog"
    page_url = reverse('blog.views.index')
    return render(request, 'blog/index.html', locals())

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    page_title = post.title
    page_url = post.get_absolute_url()

    if not post.published and not "show_unpub" in request.GET:
        raise Http404

    return render(request, 'blog/post.html', locals())