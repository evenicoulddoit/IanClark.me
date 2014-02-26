from django.conf.urls import patterns, url
from experience import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)