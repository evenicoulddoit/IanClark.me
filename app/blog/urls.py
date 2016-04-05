from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', views.Post.as_view(), name='post')
]
