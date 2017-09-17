from django.conf import settings
from django.http import Http404, HttpResponse
from django.views.generic import View


class AcmeChallenge(View):
    def get(self, *args, **kwargs):
        if settings.CERTBOT_ID == kwargs['certbot_id']:
            return HttpResponse(settings.CERTBOT_KEY)
        else:
            raise Http404
