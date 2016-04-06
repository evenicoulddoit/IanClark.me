from django.views.generic import DetailView, ListView

from blog import models as blog_models


class Index(ListView):
    """
    List all published blog posts.
    """
    template_name = 'blog/index.html'
    queryset = blog_models.Post.objects.filter(published=True)
    context_object_name = 'posts'

    def get_context_date(self):
        return dict(page_title='Blog')


class Post(DetailView):
    """
    Display an individual blog post.
    """
    template_name = 'blog/post.html'

    def get_queryset(self):
        posts = blog_models.Post.objects.all()

        if 'show_unpub' in self.request.GET:
            return posts
        else:
            return posts.filter(published=True)
