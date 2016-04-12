from django.conf.urls import url

from experience import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
