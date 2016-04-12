import markdown

from bs4 import BeautifulSoup

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def blog_markdown(value):
    table_classname = "code-snippet"

    extensions = ["nl2br", "fenced_code", "codehilite", "tables"]
    extension_configs = {
        'codehilite': [
            ("linenums", True),
            ("css_class", table_classname),
        ]
    }

    md = markdown.markdown(force_unicode(value),
                           extensions,
                           extension_configs=extension_configs,
                           safe_mode=True,
                           output_format="html5",
                           enable_attributes=False)

    soup = BeautifulSoup(md, "html.parser")
    tables = soup.find_all("table")

    for table in tables:
        responsive = soup.new_tag("div")
        responsive["class"] = "table-responsive"
        table.wrap(responsive)

    return mark_safe(soup.prettify(formatter="html"))
