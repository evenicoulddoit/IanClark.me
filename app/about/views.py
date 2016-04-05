from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self):
        return dict(site_section='about')
