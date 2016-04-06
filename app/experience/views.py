from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'experience/index.html'

    def get_context_data(self):
        return dict(
            page_title="Experience",
            active_section="experience")
