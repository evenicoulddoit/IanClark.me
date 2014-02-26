from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, render_to_response, get_object_or_404

def index(request):
    page_title = "Experience"
    page_url = reverse('experience.views.index')
    return render(request, 'experience/index.html', locals())