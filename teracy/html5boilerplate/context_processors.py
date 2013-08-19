"""
A set of request context processors provied by teracy.html5boilerplate.
"""
from django.conf import settings


def page(request):
    """
    page context processor which adds default context to 'page' via settings module.

    settings.SITE_AUTHOR => page.author
    settings.SITE_COPYRIGHT => page.copyright
    settings.SITE_GA_ID => page.ga_id
    """

    context_extras = {}

    page_context = {}

    if settings.SITE_AUTHOR is not None:
        page_context['author'] = settings.SITE_AUTHOR

    if settings.SITE_COPYRIGHT is not None:
        page_context['copyright'] = settings.SITE_COPYRIGHT

    if settings.SITE_GA_ID is not None:
        page_context['ga_id'] = settings.SITE_GA_ID

    context_extras['page'] = page_context

    return context_extras
