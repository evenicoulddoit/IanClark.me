from django.conf.urls import url
from about import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
